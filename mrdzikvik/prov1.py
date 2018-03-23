import random
import time

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def randomizedPartition(A,p,r):
    i = random.randint(p,r)
    A[r], A[i] = A[i], A[r]
    return partition(A,p,r)

def randomizedQuicksort(A,p,r):
    if p < r:
        q = randomizedPartition(A,p,r)
        randomizedQuicksort(A,p,q - 1)
        randomizedQuicksort(A,q + 1,r)

#if _name_ == "_main_":
    #A = [5,2,6,3,7,3,8,6,9]
A = random.sample(range(0, 500000), 100000)
print("Niz pre slaganja:", A)
start_time = time.clock()
randomizedQuicksort(A,0,len(A) - 1 )
end_time = time.clock() - start_time
print("Niz posle slaganja:", A)
print("Quick sort duration: ", end_time)

#10 elemenata       0.0005424354012628193
#100 elemenata      0.006329455977399189
#1000 elemenata     0.07211461059851076
#10000 elemenata    0.7453065257794771
#100000 elemenata   8.792868467806302
#1000000 elemenata  99,4219548219058