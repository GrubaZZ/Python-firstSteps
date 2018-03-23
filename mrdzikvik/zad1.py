import random
import time

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100000, 50000)

def foo(l):
    print("list: ", l)

start_time = time.clock()

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
def mergeSort(tempList):
    print("Splitting ", tempList)
    if len(tempList)>1:
        mid = len(tempList) // 2
        lefthalf = tempList[:mid]
        righthalf = tempList[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                tempList[k]=lefthalf[i]
                i=i+1
            else:
                tempList[k]=righthalf[j]
                j=j+1
            k=k+1

        # NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!
        while i < len(lefthalf):
            tempList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            tempList[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ", tempList)


foo(l)

mergeSort(l)

#NE DIRAJ SUNCE TI KALAISANO PRAVI SVOJ PROGRAM!
foo(l)

end_time = time.clock() - start_time
print("Duration: ", end_time)

#100 0.0034
#1000 0.0147
#10000 0.2
#100000 2.543

#NE DIRAJ SUNCE TI KALAISANO, PRAVI SVOJ PROGRAM!