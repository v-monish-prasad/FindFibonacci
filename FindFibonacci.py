def findFibonacci(num):
    if num == 0 or num == 1:
        return num

    return findFibonacci(num - 1) + findFibonacci(num - 2)


if __name__ == "__main__":
    number = int(input())

    print(findFibonacci(number))


# The Fibonacci numbers are the numbers in the following integer sequence.
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
#
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2
#
# Given a number A, find and return the Ath Fibonacci Number using recursion.
#
# Given that F0 = 0 and F1 = 1.
#
# Example Input
#
# Input 1:
# A = 2
#
# Input 2:
# A = 9
#
# Example Output
#
# Output 1:
# 1
#
# Output 2:
# 34
