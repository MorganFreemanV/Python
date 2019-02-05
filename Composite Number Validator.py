"""
COMPOSITE NUMBER CHALLENGE by Satnam Singh on SoloLearn

A composite number is a positive integer that is not prime.
In other words, it is a positive integer that has at least
one divisor other than 1 and itself. The composite numbers
up to 20 are 4, 6, 8, 9, 10, 12, 14, 15, 18, 20.

For example:
Input: 10
Output: yes (10 has divisors other than 1 and itself, for example, 2 or 5).

Input: 5
Output: no (5 is a prime number because it has no other divisors
other than 1 and itself).

Write a program to check if the user input is a composite number or not.
"""

# Modified the output to suit personal preference


x = int(input("Enter number: "))
statement = True
for variable in range(2, x):
    quot = x // variable
    remainder = x % variable
    if quot == x or remainder != 0:
        continue
    elif quot != x and remainder == 0:
        print("Composite number detected!")
        statement = False
        break
if statement == True:
    print('\nNot composite number!')
