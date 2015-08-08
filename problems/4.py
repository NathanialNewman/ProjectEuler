# Author: Nate Newman
# Source: Project Euler Problem 1
# Title: Largest Palindrome Product
# Description: A palindromic number reads the same both ways. 
    # The largest palindrome made from the product of two 2-digit numbers is 
    # 9009 = 91 * 99
    # Find the largest palindrome made from the product of two 3-digit numbers.

import time

def palindromeCheck(value):
    strValue = str(value)
    

    i = 0
    j = len(strValue)-1

    while(i < j):
        if strValue[i] != strValue[j]:
            return False
        else:
            i += 1
            j -= 1

    return True


def largestPalindrome():
    topValue = 999
    topPalindrome = 0

    for i in range(0,topValue):
        for j in range(0,topValue):
            pValue = (topValue-i)*(topValue-j)
            if palindromeCheck(pValue):
                if pValue > topPalindrome: topPalindrome = pValue
                break
    return topPalindrome

if __name__ == "__main__":

    start = time.time()
    # Execute code here
    print largestPalindrome()
    end = time.time()

    print "Time to complete: " + str(end-start)
