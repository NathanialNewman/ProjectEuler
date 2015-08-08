# Author: Nate Newman
# Source: Project Euler Problem 1
# Title: Multiples of 3 and 5
# Description: Find the sum of all multiples of 3 or 5 below 1000

import time

def sumMultiplesOf3and5(target):
    runningSum = 0
    for num in range(target):
        if (num % 3 == 0):
            runningSum += num
        elif (num % 5 == 0):
            runningSum += num
    
    return runningSum

if __name__ == "__main__":
    start = time.time()
    print sumMultiplesOf3and5(1000)
    end = time.time()
    print "Time to complete: " + str(end-start)
