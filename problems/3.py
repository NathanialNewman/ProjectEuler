# Author: Nate Newman
# Source: Project Euler Problem 3
# Title: Largest Prime Factor
# Description: The prime factors of 13195 are 5, 7, 13, 29
    # What is the largest prime factor of the number 600851475143 

import time

def primeFactors(target):
    largestFactor = 0
    i = 2
    while (i <= target):
        if target % i == 0:
            if largestFactor < i: largestFactor = i
            while (target % i == 0):
                target = target / i
        i += 1
    return largestFactor

if __name__ == "__main__":

    start = time.time()
    # Execute code here
    print primeFactors(600851475143)
    end = time.time()

    print "Time to complete: " + str(end-start)
