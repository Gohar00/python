'''ex1'''
'''գրել triple(data) ֆունկցիա, որը վերադարձնում է data-ի անդամների եռապատիկները պարունակող լիստ'''
# def triple(data):
#     return data * 3
# a = list(map(triple, [1, 2, 4]))
# print(a)


'''ex2'''
'''իրականացնել map3(func, data1, data2, data3) ֆունկցիա, որը վերադարձնում է նոր լիստ, որի մեջ ներառված են
func-ի կանչի արդյունքները data1, data2 և data3-ի համապատասխան անդամների անդամների վրա,
օրինակ, եթե ունենք sum(a, b, c) ֆունկցիան, որը վերադարձնում է a, b և c թվերի գումարը,
map(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]) կվերադարձնի [111, 222, 333]'''
# def map3(func, data1, data2, data3):
#     ml = []
#     tmp = []
#     j = 0
#     if len(data1) == len(data2) == len(data3):
#         print(True)
#         while j < len(data1):
#             tmp.append(data1[j])
#             tmp.append(data2[j])
#             tmp.append(data3[j])
#             a = func(tmp)
#             ml.append(a)
#             tmp.remove(data1[j])
#             tmp.remove(data2[j])
#             tmp.remove(data3[j])
#             j += 1
#         return ml
#     else:
#         return ('Data lengths are not equal')
#
# print(map3(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
# # print(map3(max, [1, 2, 3], [10, 20, 30], [100, 200, 300]))

'''ex3'''
'''իրականացնել map2(func, data1, data2) ֆունկցիա, դրա օգնությամբ գրել ծրագիր, որը կտպի էկրանին նոր լիստ, որի i-րդ անդամը կլինի bases-ի i-րդ
անդամը exp-ի i-րդ անդամով աստիճան բարձրացրած, որտեղ base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
# def map2(func, data1, data2):
#     ml = []
#     j = 0
#     if len(data1) == len(data2):
#         while j < len(data1):
#             a = pow(data1[j], data2[j])
#             ml.append(a)
#             j += 1
#         return ml
#     else:
#         return ('Data lengths are not equal')
# base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(map2(pow, base, exp))
