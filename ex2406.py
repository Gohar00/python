'''ex1'''
# def reverse(number):
#     rev_num = 0
#     while number > 0:
#         remainder = number % 10
#         rev_num = (rev_num * 10) + remainder
#         number = number // 10
#     return  rev_num
# number = int(input("Enter the number please: "))
# print(reverse(number))


'''ex2'''
# tup = (1, 2, 3, 6, 4)
# remainder = 0
# j = len(tup) - 1
# i = 1
# while j >= 0:
#     remainder += tup[j] * i
#     j -= 1
#     i *= 10
# print(remainder)


'''ex3'''
# def sum_of_min_max(data):
#     return max(data) + min(data)
# print(sum_of_min_max([10, 2, 5, 30]))

'''ex4'''
# def index(lst):
#     return [i for i in range(len(lst)) if lst[i] % 2 == 0]
# print(index([1, 2, 4, 6, 7, 8]))

'''ex5'''
# def rev_word(word):
#     nstr = ''
#     for i in word[::-1]:
#         nstr += i
#     return nstr
# mstr = input("Enter the word please: ")
# print(rev_word(mstr))

'''ex6'''
# import math
#
# def check_prime(n):
#
#     if (n <= 1):
#         return False
#     if (n <= 3):
#         return True
#     if (n % 2 == 0 or n % 3 == 0):
#         return False
#
#     for i in range(5, int(math.sqrt(n) + 1), 6):
#         if (n % i == 0 or n % (i + 2) == 0):
#             return False
#     return True
#
# def smallest_prime(n):
#
#     if (n <= 1):
#         return 2
#
#     prime = n
#     found = False
#
#     while (not found):
#         prime = prime + 1
#
#         if (check_prime(prime) == True):
#             found = True
#
#     return prime
#
# n = int(input("Please enter the number: "))
# print(smallest_prime(n))

'''ex7'''
# def get_median(data):
#
#     index = ((len(data) - 1) // 2)
#     if len(data) % 2 == 1:
#         return f'the median is: {data[index]}'
#     return f'the median is {(data[index] + data[index + 1]) / 2}'
#
# print(get_median([5, 2, 3, 8, 9, -2, 4]))


'''ex8'''
# def leap_year(year):
#     if(year % 4 == 0 and year % 100 != 0 or year %400 == 0):
#         return True
#     return False
#
# def count_of_month(year, month):
#
#         if leap_year(year):
#             if month % 2 == 1:
#                 return f' 31 day'
#             elif month == 2:
#                 return f' 29 day'
#         else:
#             if month % 2 == 0 and month != 2:
#                 return f' 30 day'
#             elif month == 2:
#                 return f' 28 day'
#
# year = int(input("Please enter the year: "))
# month = int(input("PLease enter the month: "))
# print(count_of_month(year, month))
#

'''ex9'''
# import random
#
# def random_passwd(n):
#     mstr = ''
#     for i in range(n):
#         symbol = random.randint(33, 126)
#         mstr += chr(symbol)
#     return mstr
# number = int(input("how many characters do you want the password to be? "))
# print(random_passwd(number))


'''ex10'''
# def same_parity(n, *args):
#     lst = []
#     for i in args:
#         if i % n == 0:
#             lst.append(i)
#     return lst
#
# print(same_parity(3,21,34,45,45,78,6543,2322,234))
















