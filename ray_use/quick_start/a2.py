import ray
import time
# ray.init()


@ray.remote
def double(i):
    time.sleep(0.1)
    print(f'{i = }')
    return i * 2


outputs = []
for i in range(100):
    outputs.append(double.remote(i))
outputs = ray.get(outputs)
# The double remote function is pickled and uploaded 1 time.
print(outputs)


# # A regular Python function.
# def normal_function():
#     return 1


# # By adding the `@ray.remote` decorator, a regular Python function
# # becomes a Ray remote function.
# @ray.remote
# def my_function(a =1):
#     return [a * 2, a * 3], [a * 4, a * 5]


# # To invoke this remote function, use the `remote` method.
# # This will immediately return an object ref (a future) and then create
# # a task that will be executed on a worker process.
# # obj_ref = my_function.remote()

# ref1, ref2 = my_function.options(num_returns=2).remote(a=2)
# result1 = ray.get(ref1)
# result2 = ray.get(ref2)
# print(f'{result1 = }')
# print(f'{result2 = }')

# # Returns one ObjectRef containing a tuple
# ref = my_function.options(num_returns=1).remote(a=2)
# result = ray.get(ref)  # result is a tuple: ([4, 6], [8, 10])
# print(f'{result = }')

# # # The result can be retrieved with ``ray.get``.
# # print(ray.get(obj_ref))
# r = ray.get(my_function.options(num_returns=1, max_retries=0).remote(a=2))
# # r = ([4, 6], [8, 10])
# print(f'{r = }')

# @ray.remote
# def slow_function():
#     time.sleep(3)
#     return 1

# start_time = time.time()
# # Ray tasks are executed in parallel.
# # All computation is performed in the background, driven by Ray's internal event loop.
# results = []
# for _ in range(10):
#     # This doesn't block.
#     results.append(slow_function.remote())
# results = ray.get(results)
# print(f'{type(results) = }')
# end_time = time.time()
# print("Time taken to start 4 tasks:", end_time - start_time)
# for item in results:
#     # ObjectRef(1e8ff6d236132784ffffffffffffffffffffffff0100000001000000)
#     print(item)

# @ray.remote(num_cpus=4, num_gpus=2)
# def my_function():
#     return 1


# @ray.remote
# def function_with_an_argument(value):
#     return value + 1


# obj_ref1 = my_function.remote()
# # assert ray.get(obj_ref1) == 1

# # You can pass an object ref as an argument to another Ray task.
# obj_ref2 = function_with_an_argument.remote(obj_ref1)
# assert ray.get(obj_ref2) == 2