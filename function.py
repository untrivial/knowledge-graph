import random

def add_to_list(result: list) -> None:
    temp = []
    for i in range(random.randint(5000000,9999999)):
        temp.append(i)
    result.append(temp)

def add_to_list_wrapper(queue):
    result = []
    add_to_list(result)
    queue.put(result)
