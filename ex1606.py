'''contain'''
# def contain(data, val):
#     if val in data:
#         return True
#     return False
# print(contain([1,3,4], 2))


'''pop first option'''
# def pop(data, i = None):
#
#     val = data[-1]
#     j = 0
#     new_list = []
#     if i == None:
#         new_list = data[:-1]
#     else:
#         while j < len(data):
#             if i == data[j]:
#                 val = i
#                 i = j
#             j += 1
#             new_list = data[:i] + data[i + 1:]
#
#     return f"new-list: {new_list}  val: {val}"
# data = [7, 1, 4, 3, 5, 6, 7, 'a']
# print(pop(data, 2))

'''remove'''
# def  remove_all(data, val):
#
#     j = 0
#     new_list = []
#     count = 0
#
#     while j < len(data):
#         if val != data[j]:
#             new_list.append(data[j])
#         j += 1
#
#     return f"new-list: {new_list}"
#
# data = [1, 7, 4, 3, 5, 7, 6, 7, 'a']
# value = 7
# print(remove_all(data, value))


'''reverse'''
# def reverse(data):
#
#     new_list = []
#     j = len(data) - 1
#     while j >= 0:
#         new_list.append(data[j])
#         j -= 1
#     return new_list
# print(reverse([1, 2, 34, 5, 7]))

'''max'''
# def max(data):
#
#     j = 0
#     i = data[0]
#     while j < len(data):
#         if data[j] >= i:
#             i = data[j]
#         j += 1
#     return i
# print(max([-1, -5, -2, -1]))

'''min'''
# def min(data):
#     j = 0
#     i = data[0]
#     while j < len(data):
#         if data[j] <= i:
#             i = data[j]
#         j += 1
#     return i
# print(min([-1, -5, -2, -1]))
