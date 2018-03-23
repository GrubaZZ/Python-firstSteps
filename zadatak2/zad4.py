import random
import time
import zad1

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def foo(l):
    print("list: ", l)

zad1.insertionSort(l)

start_time = time.clock()

def binary_search(obj, item):
    lo, hi = 0, len(obj) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if obj[mid] < item:
            lo = mid + 1
        elif item < obj[mid]:
            hi = mid - 1
        else:
            return mid
    return None

print(binary_search(l,48))


end_time = time.clock() - start_time
print("Duration: ", end_time)