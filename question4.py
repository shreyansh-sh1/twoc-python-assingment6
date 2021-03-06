def findGreaterNum(digits, n):
    # traverse the digits to find if they are in some order
    for i in range(n - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            # this means digits are not in descending order
            break

    if i == 0:
        # means we traversed all the digits and found them in descending order
        print("This is the greatest number")

    # if in the for loop above break is executed, means we found
    # a number smaller than its predecessor while moving towards left from right
    x = digits[i - 1]
    pos = i
    for j in range(i + 1, n):
        if digits[j] > x and digits[j] < digits[pos]:
            pos = j

    # swapping the numbers at position j and i-1
    digits[i - 1], digits[pos] = digits[pos], digits[i - 1]

    result = 0
    for j in range(i):
        result = result * 10 + digits[j]

    # sort the digits after i-1 in ascending order
    digits = sorted(digits[i:])

    for j in range(n - i):
        result = result * 10 + digits[j]

    print("The next number with same set of digits is: ", result)


# Let's take a number from user input
number = input("Please enter a number: ")

# We need to create a list with all the digits in the number
digits = list(map(int, number))
findGreaterNum(digits, len(number))

# code by shreyansh sharma