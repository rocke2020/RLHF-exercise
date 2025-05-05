import ray
import asyncio
from time import sleep


@ray.remote
class TaskStore:
    def get_next_task(self):
        sleep(1)  # Simulate a blocking operation
        return "task"


@ray.remote
class AsyncTaskExecutor:
    def __init__(self, task_store):
        self.task_store = task_store
        self.num_executed_tasks = 0

    async def run(self):
        while True:
            # Here we use await instead of ray.get() to
            # wait for the next task and it will yield
            # the control while waiting.
            task = await task_store.get_next_task.remote()
            # TODO I don't know why _execute_task is not executed
            self._execute_task(task)

    def _execute_task(self, task):
        # Executing the task
        self.num_executed_tasks = self.num_executed_tasks + 1

    def get_num_executed_tasks(self):
        return self.num_executed_tasks

task_store = TaskStore.remote()
async_task_executor = AsyncTaskExecutor.remote(task_store)
async_task_executor.run.remote()
# We are able to run get_num_executed_tasks while run method is running.
num_executed_tasks = ray.get(async_task_executor.get_num_executed_tasks.remote())
print(f"num of executed tasks so far: {num_executed_tasks}")