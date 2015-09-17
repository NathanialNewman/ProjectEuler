# Author: Nate Newman
# Source: Project Euler Problem 
# Title: Largest product in a series
# Description: The four adjacent digits in the 1000-digit
    # number that have the greates product are 
    # 9 x 9 x 8 x 9 = 5832
    # Find the 13 adjacent digits in the 1000-digit number that have the greatest product.
    # What is teh value of this product 

import time
import os
from operator import mul

# Takes in a number of adjacent digits (num)
# and a list of digits (inputList)
# and returns a list of size num which has the greatest product
def findGreatestAdjacentProduct(num, inputList):
    maxList = []
    testList = []

    for i in range(len(inputList)):
        if len(testList) < num:
            testList.append(inputList[i])
        else:
            if (testList[0] < inputList[i]):
                testList.pop(0)
                testList.append(inputList[i])
            else:
                testList = []

            if (reduce(mul,testList,1) > reduce(mul,maxList,1)):
                maxList = testList

    return maxList

if __name__ == "__main__":

    start = time.time()
    # Execute code here

    # Find path of script and navigate to resource
    scriptDir = os.path.dirname(__file__)
    relPath = "resources/8.txt"
    absPath = os.path.join(scriptDir, relPath)

    # Create list from file
    digitList = []
    with open(absPath) as f:
        c = f.read(1)
        while c:
            if c != '\n':
                digitList.append(int(c))
            c = f.read(1)

    ansList = (findGreatestAdjacentProduct(13, digitList))
    print(ansList)
    print(reduce(mul,ansList,1))

    end = time.time()

    print "Time to complete: " + str(end-start)
