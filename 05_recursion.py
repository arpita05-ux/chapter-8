'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2*1
factorial(3) = 3*2*1
factorial(4) = 4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(n) = n * n-1 *......*3 *2 * 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)   #recursive call

n = int(input("enter your number: "))
print(f"The factorial of this number is:{factorial(n)}")


# Recursion is a method where a function solves a problem by calling itself with a smaller version of the same problem.

