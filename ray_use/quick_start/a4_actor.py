import ray

@ray.remote
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def get_counter(self):
        return self.value

# Create an actor from this class.
# counter = Counter.remote()

import time

@ray.remote
def f(counter):
    for _ in range(10):
        time.sleep(0.1)
        counter.increment.remote()


counter = Counter.remote()

# Start some tasks that use the actor.
# f.remote runs in parallel with the actor.
# This will run 3 tasks in parallel.
[f.remote(counter) for _ in range(3)]

# Print the counter value.
for _ in range(10):
    time.sleep(0.1)
    print(ray.get(counter.get_counter.remote()))