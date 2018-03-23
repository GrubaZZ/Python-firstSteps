import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def foo(l):
    print("list: ", l)

start_time = time.clock()

def linear_search(obj, item, start=0):
    for i in range(start, len(obj)):
        if obj[i] == item:
            return i
    return -1

print(linear_search(l,48))

foo(l)

end_time = time.clock() - start_time
print("Duration: ", end_time)