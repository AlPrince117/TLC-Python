# LAB 1

# Question 2
# number = int(input("Please enter your number : "))
# if number % 2 == 0:
#     print("This number is an even number")
# else:
#     print("This number is an odd number")





# QUESTION 3
# name = "Phelim"
# age = 23
# print(name)
# print(age)
#
#
# nameAge = name + str(age)
# nameAges = f"{name} is {age}"
# print(nameAges)

# QUESTION 4
# import random
# guess = int(input("Please enter your guess :"))
# rand = random.randrange(2, 10, 2)
# condition = True
# while condition:
#     if guess == rand:
#         print("You got it right")
#         condition = False
#
#     else:
#         print("Try again")
#         guess = int(input("Please enter your guess :"))


# Question 5
# alist = [1, 4, 9, 16, 25]
# for i in alist:
#     if i % 2 == 0:
#         print(i)

# Question 6

# n = 23
# i = 0
# while n > 0:
#
#     i = i + n
#     n = n - 1
#
#     print("some of myAge is ", i)

# currentAge =10
# start = 1
# sum_of_years = 0
#
# while start <= currentAge:
#
#     sum_of_years += start
#
#     start += 1
#
# print(f"you are {sum_of_years} years {sum_of_years *12} months {sum_of_years*30.4 *12}{sum_of_years*730*12} hours" )

# LAB 2

# QUESTION 5
# print(type(5))
# print(type(5000 * 50000000))
# print(type('j'))
# print(type(1j))
# print(type((1,)))
# print(type([5]))
# print(type(None))

# QUESTION 6
# from decimal import Decimal
# print(.1 + .1 + .1)
# print(Decimal(".1") + Decimal(".1") + Decimal(".1"))


# QUESTION 7

# numberOFterms = int(input("How many terms? "))
#
# # first two terms
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
# if numberOFterms <= 0:
#     print("Please enter a positive integer")
# elif numberOFterms == 1:
#     print("Fibonacci sequence up to", numberOFterms, ":")
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < numberOFterms:
#         print(n1)
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1


# QUESTION 8a
# name = "Phelim"
# print(name[-1])

# QUESTION 8b

name = "Phelim"
for n in name:
    print(n, end=":")

# QUESTION 9

count = 0


# QUESTION 10

# alist = [1, 4, 9, 16, 25]
# print('alist: ', alist)
#
# newlist = [x for x in alist if x%2 != 0]
# print(newlist)
