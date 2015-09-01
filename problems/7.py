# Author: Nate Newman
# Source: Project Euler Problem 
# Title: 10001st prime
# Description: By listing the first six prime numbers:
    # 2, 3, 5, 7, 11, and 13
    # we can see that the 6th prime is 13.
    # What is the 10001st prime number 

import time
from math import log
from math import floor

def sieve (limit, index):
    fullList = [True]*limit

    fullList[0] = fullList[1] = False

    for i in range(limit):
        if fullList[i]:
            for j in range(i*i, limit, i):
                fullList[j] = False

    primeIndex = 0
    for i in range(len(fullList)):
        if fullList[i]:
            primeIndex += 1
            if (primeIndex == index):
                return i

if __name__ == "__main__":

    start = time.time()

    limit = 10001*log(10001) + 10001*(log(log(10001)))
    fLimit = floor(limit)

    print(sieve(int(fLimit), 10001))
    # Execute code here
    end = time.time()

    print "Time to complete: " + str(end-start)
