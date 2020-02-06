from timeit import default_timer as time
import collections
import numpy as np
import matplotlib.pyplot as plt







def insertionSort(list):

    index = range(1, len(list)) #all the values after the 1st
    for i in index:
        sort = list[i] #value to sort

        while list[i-1] > sort and i > 0:
            list[i], list[i-1] = list[i-1], list[i]
            i -= 1


    return list













def mergeSort(list):


    if len(list) <= 1:
        return list
    mid = int(len(list) / 2)
    left =  mergeSort(list[:mid])
    right = mergeSort(list[mid:])


    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result





i = 4
digits = []
merg_elapsed = []
ins_elapsed = []
while i != 0:
    if i == 4:
        def createMerge_Array(size=10, max=50):
            from random import randint
            list = [randint(0, max) for _ in range(size)]
            digits.append(size)
            return list
        m = createMerge_Array()

        def ins():
            insrt_start = time()
            print(insertionSort(m))
            insrt_end = time()
            insrt_time = insrt_end - insrt_start
            ins_elapsed.append(insrt_time)
            return insrt_time
        print(ins(), "Insertion")
        def merg():
            merg_start = time()
            print(mergeSort(m))
            merge_end = time()
            merg_time = merge_end - merg_start
            merg_elapsed.append(merg_time)
            return merg_time
        print(merg(), "Merged\n")
        i -= 1

    elif i == 3:
        def createMerge_Array(size=100, max=50):
            from random import randint
            list = [randint(0, max) for _ in range(size)]
            digits.append(size)
            return list
        m = createMerge_Array()

        def ins():
            insrt_start = time()
            print(insertionSort(m))
            insrt_end = time()
            insrt_time = insrt_end - insrt_start
            ins_elapsed.append(insrt_time)
            return insrt_time
        print(ins(), "Insertion")
        def merg():
            merg_start = time()
            print(mergeSort(m))
            merge_end = time()
            merg_time = merge_end - merg_start
            merg_elapsed.append(merg_time)
            return merg_time
        print(merg(), "Merged\n")
        i -= 1

    elif i == 2:
        def createMerge_Array(size=1000, max=50):
            from random import randint
            list = [randint(0, max) for _ in range(size)]
            digits.append(size)
            return list
        m = createMerge_Array()

        def ins():
            insrt_start = time()
            print(insertionSort(m))
            insrt_end = time()
            insrt_time = insrt_end - insrt_start
            ins_elapsed.append(insrt_time)
            return insrt_time
        print(ins(), "Insertion")
        def merg():
            merg_start = time()
            print(mergeSort(m))
            merge_end = time()
            merg_time = merge_end - merg_start
            merg_elapsed.append(merg_time)
            return merg_time
        print(merg(), "Merged\n")
        i -= 1

    elif i == 1:
        def createMerge_Array(size=10000, max=50):
            from random import randint
            list = [randint(0, max) for _ in range(size)]
            digits.append(size)
            return list
        m = createMerge_Array()

        def ins():
            insrt_start = time()
            print(insertionSort(m))
            insrt_end = time()
            insrt_time = insrt_end - insrt_start
            ins_elapsed.append(insrt_time)
            return insrt_time
        print(ins(), "Insertion")
        def merg():
            merg_start = time()
            print(mergeSort(m))
            merge_end = time()
            merg_time = merge_end - merg_start
            merg_elapsed.append(merg_time)
            return merg_time
        print(merg(), "Merged\n")
        i -= 1


print(digits)
print(ins_elapsed)
print(merg_elapsed)





fig, ax = plt.subplots()
index = np.arange(4)

plt.figure(1)
plt.plot(ins_elapsed, color = 'b', label='Insertion Sort')
plt.xlabel('Number of Digits')
plt.ylabel('Elapsed Time')
plt.title('Insertion Sort\n(Execution Time)')
plt.xticks(index, (digits))
plt.legend()

plt.figure(2)

bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, merg_elapsed, bar_width, alpha=opacity, color='r', label='Merge Sort')
plt.xlabel('Number of Digits')
plt.ylabel('Elapsed Time (milliseconds)')
plt.title('Merge Sort\n(Execution Time)')
plt.xticks(index, (digits))
plt.legend()




# OR PWEDE PUD KANI MAAM KASO DI MAKLARO ANG TIME SA MERGE KAY GAMAY KAAYO ICOMPARE SA INSERTION
'''
plt.plot(merg_elapsed, color = 'r', label='Merge Sort')
plt.plot(ins_elapsed, color = 'b', label='Insertion Sort')
plt.xlabel('Number of Digits')
plt.ylabel('Time elapsed')
plt.title('Merge Sort VS Insertion Sort\n(Execution Time)')
plt.xticks(index, (digits))
plt.legend()
'''


plt.tight_layout()
plt.show()











