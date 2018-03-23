import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def foo(l):
    print("list: ", l)

def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def Max_Heapify(A,i):
    l=left(i)
    r=right(i)
    if l+1 < len(A) and A[l]>A[i]:
        largest = l
    else: largest = i
    if r+1 < len(A) and A[r]>A[largest]:
        largest=r
    if largest != i:
        A[i],A[largest]=A[largest],A[i]
        Max_Heapify(A,largest)

def Build_Max_Heap(A):
    size=len(A)
    for i in range(size//2, 0, -1):
        Max_Heapify(A,i)

def Heapsort(A):
    Build_Max_Heap(A)
    size=len(A)
    for i in range(size,1,-1):
        A[1],A[i]=A[i],A[1]
        size=size-1
        Max_Heapify(A,1)




start_time = time.clock()


print(Heapsort(l))


end_time = time.clock() - start_time
print("Duration: ", end_time)