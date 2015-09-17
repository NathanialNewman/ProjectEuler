# Author: Nate Newman
# Source: Project Euler Problem 6
# Title: Sum Square Difference
# Description: The Sum of the squares of the first ten natural numbers is 
    # 1^2 + 2^2 + ... + 10^2 = 385
    # The square of the sum of the first to natural numbers is
    # (1 + 2 + ... + 10)^2 = 55^2 = 3025
    # Hence the difference between the sum of squares and square of the sum is
    # 3025 - 385 = 2640
    # Find the difference between the sum of squares and square of the sum for 
    # the first 100 natural numbers

import time

def sumOfSquares(limit):
    sumOS = 0
    for i in range (1,limit+1):
        sumOS += (i*i)

    return sumOS

def squareOfSum(limit):
   
    if (limit % 2 == 0):
        sumToLimit = (limit+1)*(limit/2)
        return sumToLimit*sumToLimit    
    else:
        sumToLimit = limit + (limit)*((limit-1)/2)
        return sumToLimit*sumToLimit

if __name__ == "__main__":

    start = time.time()
    # Execute code here
    print squareOfSum(100) - sumOfSquares(100)
    end = time.time()

    print "Time to complete: " + str(end-start)
