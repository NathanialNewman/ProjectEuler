# Author: Nate Newman
# Source: Project Euler Problem 9
# Title: Special Pythagorean Triplet
# Description: There exists exactly 1 Pythagorean triplet for which
    # a + b + c = 1000
    # Find the product a*b*c

import time

# Determines if set of 3 values form a Pythagorean Triple
def pythagTriplet(a, b, c):
    triplets = [a,b,c]
    triplets.sort()
    
    return ((triplets[0]*triplets[0]) + 
        (triplets[1]*triplets[1]) ==
        (triplets[2]*triplets[2]))

# Finds 3 numbers that add to 'target' which are a pythagorean triplet
def find3SumTarget(target):
    for i in range(1,target):
        for j in range(1,target):
            if pythagTriplet(i,j,(1000-i-j)):
                return[i,j,(1000-i-j)]

if __name__ == "__main__":

    start = time.time()

    # Execute code here
    foundSet = find3SumTarget(1000)
    print (foundSet[0]*foundSet[1]*foundSet[2])

    end = time.time()

    print "Time to complete: " + str(end-start)
