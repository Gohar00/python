"""ex1.5"""
# def sum_of_number(a, b):
#     sum = 0
#     while a <= b:
#         sum += a
#         a += 1
#     return sum
# print(sum_of_number(1, 3))

"""ex1.6"""
# def sum_of_number(a, b):
#     sum = 0
#     if a >= b:
#         tmp = a
#         a = b
#         b = tmp
#         while a <= b:
#             sum += a
#             a += 1
#     return sum
# print(sum_of_number(3, 1))

"""ex1.7"""
# def pow(base, exp):
#     res = 1
#     count = 0
#     if base == 0 and exp < 0:
#         return "meaningless expression"
#     elif exp < 0:
#         while count < -exp:
#             res = res * (1 / base)
#             count += 1
#     elif exp == 0:
#         return res
#     else:
#         while count < exp:
#             res = res * base
#             count += 1
#
# print(pow(2, 0))

"""ex1.8"""
def abs(n):
    if n > 0:
        return n
    else:
        return -n

def guess_enough(value, target):
    if abs(value**3 - target) < 0.0001:
        return True
    else:
        return False

def improve(root, target):
    return ((target / (root ** 2)) + (2 * root)) /3

def cubrt(n):
    root = 1
    while not guess_enough(root, n):
        root = improve(root, n)
    return root

print(cubrt(3))
