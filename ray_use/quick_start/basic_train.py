import ray.train.torch
import torch
import torch.nn as nn

from ray.train import ScalingConfig
from ray.train.torch import TorchTrainer
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

from utils_comm.log_util import logger


def get_dataset():
    return datasets.FashionMNIST(
        root="/data/comm",
        train=True,
        download=True,
        transform=ToTensor(),
    )


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, inputs):
        inputs = self.flatten(inputs)
        logits = self.linear_relu_stack(inputs)
        return logits


def train_func():
    num_epochs = 1
    batch_size = 64

    dataset = get_dataset()
    for item in dataset:
        print(type(item))
        input_data, label = item
        print(input_data.shape)
        break
    dataloader = DataLoader(dataset, batch_size=batch_size)

    model = NeuralNetwork()

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(num_epochs):
        for inputs, labels in dataloader:
            optimizer.zero_grad()
            pred = model(inputs)
            loss = criterion(pred, labels)
            loss.backward()
            optimizer.step()
        print(f"epoch: {epoch}, loss: {loss.item()}")


def train_func_distributed():
    num_epochs = 3
    batch_size = 64

    # Ensure dataset is properly serialized
    dataset = get_dataset()
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    dataloader = ray.train.torch.prepare_data_loader(dataloader)

    # Ensure model is properly serialized
    model = NeuralNetwork()
    model = ray.train.torch.prepare_model(model)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(num_epochs):
        if ray.train.get_context().get_world_size() > 1:
            dataloader.sampler.set_epoch(epoch)

        for inputs, labels in dataloader:
            optimizer.zero_grad()
            pred = model(inputs)
            loss = criterion(pred, labels)
            loss.backward()
            optimizer.step()
        logger.info(f"epoch: {epoch}, loss: {loss.item()}")


# For GPU Training, set `use_gpu` to True.
use_gpu = True

trainer = TorchTrainer(
    train_func_distributed, scaling_config=ScalingConfig(num_workers=3, use_gpu=use_gpu)
)

results = trainer.fit()
