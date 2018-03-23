import random
import time

def insertionSort(alist):
   for index in range(1,len(alist)):

     key = alist[index]
     position = index

     while position>0 and alist[position-1]>key:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=key

 range(min, max), elements)
        return listy

    l = random_list(1, 10000, 1000)

    def foo(l):
        print("list: ", l)

    start_time = time.clock()



    insertionSort(l)

    foo(l)

    end_time = time.clock() - start_time
    print("Duration: ", end_time)

    print("TEST ")



