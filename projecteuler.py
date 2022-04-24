#!/usr/bin/python3
import sys


# Multiples of 3 or 5
def prob1():
    sum = 0
    for i in range(10):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
        print(i, sum)
    print(sum)


# Fibonacci
def prob2():
    i = 1  # First term
    j = 1  # Second term
    k = 0  # Transition Term
    sum = 0
    while j < 4000000:
        if (i + j) % 2 == 0:  # only sum even terms
            sum += (i + j)
        k = i + j
        i = j
        j = k
    print(sum)


# Prime Factors
def prob3(x):
    prime_factors = []
    while not isprime(x):
        for i in range(2, x):
            if isprime(i) and (x % i == 0):
                # print(i, x)
                prime_factors.append(i)
                x = x // i  # Python3 requires // for integer division
                break
    prime_factors.append(x)
    print(prime_factors)


# Largest Palindrome Product
def prob4(x):
    end = False
    i = 1
    j = 1
    highest_palindrome = 0

    while i < 999:
        while j < 999:
            if ispalindrome(i * j) and (i * j > highest_palindrome):
                highest_palindrome = i * j
                # print(i, j, i * j)
            j += 1
        i += 1
        j = 1
    return highest_palindrome


# Smallest Multiple
# What is the smallest positive number evenly divisible by all number from 1 to 20?
def prob5():
    count = 2
    found = False
    div_nums = 20
    while not found:
        for i in range(1, div_nums + 1, 1):
            if i == div_nums:
                found = True
                print(count)
            elif count % i != 0:
                count += 1
                # print(count)
                break



''' ********* HELPER FUNCTIONS ********* '''


# Returns true is num is prime
def isprime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


# Returns true if the num is a palindrome
def ispalindrome(num):
    pal = [int(i) for i in str(num)]
    palrev = pal.copy()
    palrev.reverse()  # Reverse changes the list it is given, it doesn't return a value
    for i in range(len(pal)):
        if pal[i] != palrev[i]:
            return False
    return True


''' ********* MAIN FUNCTION ********* '''
if __name__ == "__main__":
    # prob1()
    # prob2()
    # prob3(600851475143)
    # prob4(999)
    prob5()

sys.exit(0)
