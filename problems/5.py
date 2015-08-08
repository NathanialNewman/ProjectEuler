# Author: Nate Newman
# Source: Project Euler Problem 5
# Title: Smallest Multiple
# Description: 2520 is the smallest number that can be divided 
    # by each of the numbers from 1 to 10 without any remainder.
    # What is the smallest positive number that is evenly divisible 
    # by all of the numbers from 1 to 20?

import time

# Generate Prime factors for the target and add them 
# and their counts to a dictionary
def primeFactors(target):
    currentDict = {}
    i = 2
    while (i <= target):
        if target % i == 0:
            currentDict[i] = 1
            target = target / i
            while (target % i == 0):
                target = target / i
                currentDict[i] += 1
        i += 1
    return currentDict

# Generate the union of allDict and the primeFactors dicitonary
# of the target number
    # Example if target A = {"3":1, "5":2} and allDict = {"3":4, "5":1}
    # this would set allDict = {"3":4, "5":2}
def matchFactors(target, allDict):
    currentDict = primeFactors(target)

    for i in currentDict:
        if i in allDict: 
            if currentDict[i] > allDict[i]: allDict[i] = currentDict[i]
        else:
            allDict[i] = currentDict[i] 

# Calculate the product of all values in a set
def dictProduct(allDict):
    product = 1
    for i in allDict:
        for j in range(allDict[i]):
            product *= i
    return product

if __name__ == "__main__":

    start = time.time()
    allDict = {}

    # Generate set of all prime factors for the numebers 1-20
    # without duplicates
    for i in range(20): matchFactors(i, allDict)

    print dictProduct(allDict)
     
    end = time.time()

    print "Time to complete: " + str(end-start)
