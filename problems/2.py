# Author: Nate Newman
# Source: Project Euler Problem 1
# Title: Even Fibonacci Numbers 
# Description: Each new term in the Fibonacci sequence is generated 
    # by adding the previous two terms. 
    # By starting with 1 and 2, the first 10 terms will be: 
    #    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    # By considering the terms in the Fibonacci sequence 
    # whose values do not exceed four million, 
    # find the sum of the even-valued terms.

import time

def sumEvenFibonacci(target):
    f1 = 1
    f2 = 2
    runningSum = 2

    while (f1 <= target):
        newf = f1 + f2
    
        if (newf > target):
            return runningSum

        elif (newf % 2 == 0):
            runningSum += newf
    
        if (f1 < f2):
            f1 = newf
        else:
            f2 = newf

    return runningSum


if __name__ == "__main__":

    start = time.time()
    print sumEvenFibonacci(4000000)
    end = time.time()

    print "Time to complete: " + str(end-start)

