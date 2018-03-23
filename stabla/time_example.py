import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def foo(l):
    print("list: ", l)

start_time = time.clock()

import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def foo(l):
    print("list: ", l)

start_time = time.clock()

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

bubbleSort(l)


foo(l)

end_time = time.clock() - start_time
print("Duration: ", end_time)

