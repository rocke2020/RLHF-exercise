import ray

# ray.init()


@ray.remote
def double(i):
    return i * 2


outputs = []
for i in range(10):
    outputs.append(double.remote(i))
outputs = ray.get(outputs)
# The double remote function is pickled and uploaded 1 time.
print(outputs)
