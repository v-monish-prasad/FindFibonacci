def findFibonacci(num):
    if num == 0 or num == 1:
        return num

    return findFibonacci(num - 1) + findFibonacci(num - 2)


if __name__ == "__main__":
    number = int(input())

    print(findFibonacci(number))
