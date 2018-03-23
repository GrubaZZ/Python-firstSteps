import random
import time
#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 10000, 5000)

def foo(l):
    print("list: ", l)

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
start_time = time.clock()

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   # NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


foo(l)

quickSort(l)

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
foo(l)

end_time = time.clock() - start_time
print("Duration: ", end_time)

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!