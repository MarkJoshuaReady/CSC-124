from timeit import default_timer as time
import math
import numpy as np
import matplotlib.pyplot as plt


def fib1(n):
    if n <= 1:
        return n
    else:
        return (fib1(n - 1) + fib1(n - 2))


def fib1Input(x):
    fib= []
    if x <= 0:
        print("Incorrect input")
    else:
        for i in range(x):
            fib.append(fib1(i))
    print(fib , " Recursive")

#fib1Input(12)








def fib2(n):
    a = 0
    b = 1
    count = 0
    fib = []
    if n <= 0:
        print("Incorrect Input")
    elif n == 1:
        return print(a)
    else:
        while count < n:
            fib.append(a)
            nth = a + b
            a = b
            b = nth
            count += 1
    print(fib , " Iterative")
#fib2(12)








def fib3(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        fib.append(a)
    print(fib)








fib1Time = []
fib2Time = []
fib3Time = []
terms = []

i = 5
while i != 0:
    if i == 5:
        n = 7
        def fibo1(n):
            fib1Start = time()
            fib1Input(n)
            fib1End = time()
            fibo1time = fib1End - fib1Start
            fib1Time.append(fibo1time)
            return fibo1time
        print(fibo1(n), " Recursive with 7 terms input Elapsed time")

        def fibo2(n):
            fib2Start = time()
            fib2(n)
            fib2End = time()
            fibo2time = fib2End - fib2Start
            fib2Time.append(fibo2time)
            return fibo2time
        print(fibo2(n), " Iterative with 7 terms input Elapsed time")

        def fibo3(n):
            fib3Start = time()
            fib3(n)
            fib3End = time()
            fibo3time = fib3End - fib3Start
            fib3Time.append(fibo3time)
            return fibo3time


        print(fibo3(n), " Option 3 with 7 terms input Elapsed time\n\n")
        terms.append(n)
        i -= 1



    elif i == 4:
        n = 14
        def fibo1(n):
            fib1Start = time()
            fib1Input(n)
            fib1End = time()
            fibo1time = fib1End - fib1Start
            fib1Time.append(fibo1time)
            return fibo1time


        print(fibo1(n), " Recursive with 14 terms input Elapsed time")


        def fibo2(n):
            fib2Start = time()
            fib2(n)
            fib2End = time()
            fibo2time = fib2End - fib2Start
            fib2Time.append(fibo2time)
            return fibo2time


        print(fibo2(n), " Iterative with 14 terms input Elapsed time")


        def fibo3(n):
            fib3Start = time()
            fib3(n)
            fib3End = time()
            fibo3time = fib3End - fib3Start
            fib3Time.append(fibo3time)
            return fibo3time


        print(fibo3(n), " Option 3 with 14 terms input Elapsed time\n\n")
        terms.append(n)
        i -= 1



    elif i == 3:
        n = 21
        def fibo1(n):
            fib1Start = time()
            fib1Input(n)
            fib1End = time()
            fibo1time = fib1End - fib1Start
            fib1Time.append(fibo1time)
            return fibo1time


        print(fibo1(n), " Recursive with 21 terms input Elapsed time")


        def fibo2(n):
            n = 21
            fib2Start = time()
            fib2(n)
            fib2End = time()
            fibo2time = fib2End - fib2Start
            fib2Time.append(fibo2time)
            return fibo2time


        print(fibo2(n), " Iterative with 21 terms input Elapsed time")


        def fibo3(n):
            fib3Start = time()
            fib3(n)
            fib3End = time()
            fibo3time = fib3End - fib3Start
            fib3Time.append(fibo3time)
            return fibo3time


        print(fibo3(n), " Option 3 with 21 terms input Elapsed time\n\n")
        terms.append(n)
        i -= 1

    elif i == 2:
        n = 28
        def fibo1(n):
            fib1Start = time()
            fib1Input(n)
            fib1End = time()
            fibo1time = fib1End - fib1Start
            fib1Time.append(fibo1time)
            return fibo1time


        print(fibo1(n), " Recursive with 28 terms input Elapsed time")


        def fibo2(n):
            fib2Start = time()
            fib2(n)
            fib2End = time()
            fibo2time = fib2End - fib2Start
            fib2Time.append(fibo2time)
            return fibo2time


        print(fibo2(n), " Iterative with 28 terms input Elapsed time")


        def fibo3(n):
            fib3Start = time()
            fib3(n)
            fib3End = time()
            fibo3time = fib3End - fib3Start
            fib3Time.append(fibo3time)
            return fibo3time


        print(fibo3(n), " Option 3 with 28 terms input Elapsed time\n\n")
        terms.append(n)
        i -= 1



    elif i == 1:
        n = 35
        def fibo1(n):
            fib1Start = time()
            fib1Input(n)
            fib1End = time()
            fibo1time = fib1End - fib1Start
            fib1Time.append(fibo1time)
            return fibo1time


        print(fibo1(n), " Recursive with 35 terms input Elapsed time")


        def fibo2(n):
            fib2Start = time()
            fib2(n)
            fib2End = time()
            fibo2time = fib2End - fib2Start
            fib2Time.append(fibo2time)
            return fibo2time


        print(fibo2(n), " Iterative with 35 terms input Elapsed time")


        def fibo3(n):
            fib3Start = time()
            fib3(n)
            fib3End = time()
            fibo3time = fib3End - fib3Start
            fib3Time.append(fibo3time)
            return fibo3time


        print(fibo3(n), " Option 3 with 35 terms input Elapsed time\n\n")
        terms.append(n)
        i -= 1




print(fib1Time, " RECURSIVE LIST OF ELAPSED TIME WITH NUMBER OF TERMS (7 ,14, 21, 28, 35)")
print(fib2Time, " ITERATIVE LIST OF ELAPSED TIME WITH NUMBER OF TERMS (7 ,14, 21, 28, 35)")
print(fib3Time, " OPTION 3 LIST OF ELAPSED TIME WITH NUMBER OF TERMS (7 ,14, 21, 28, 35)")
print(terms, " SIZE TERMS")




fig, ax = plt.subplots()
index = np.arange(len(terms))


plt.plot(fib1Time, color = 'b', label='Recursive')
plt.xlabel('Number of Terms')
plt.ylabel('Elapsed Time(seconds)')
plt.title('Fibonacci\n(Execution Time)')
plt.xticks(index, (terms))
plt.legend()



plt.figure(2)
bar_width = 0.35


rects1 = plt.bar(index - 0.08, fib3Time, bar_width/2, color='g', label='Option 3')
rects2 = plt.bar(index + 0.08, fib2Time, bar_width/2, color='r', label='Iterative')
plt.xlabel('Number of Terms')
plt.ylabel('Elapsed Time(seconds)')
plt.title('Fibonacci\n(Execution Time)')
plt.xticks(index, (terms))
plt.legend()




plt.tight_layout()
plt.show()
