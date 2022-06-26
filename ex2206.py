'''ex1'''
'''Գրել ծրագիր, որը օգտատիրոջից սպասում է մուտք՝ բառերի ցանկ, մինչև օգտագործողը թողնի մուտքագրման տողը դատարկ: 
Դրանից հետո օգտատիրոջ մուտքագրած բառերը պետք է ցուցադրվեն էկրանին, բայց առանց կրկնությունների՝ յուրաքանչյուրը մեկ անգամ։ 
Այս դեպքում բառերը պետք է ցուցադրվեն նույն հաջորդականությամբ, որով դրանք մուտքագրվել են ստեղնաշարից'''
# def words(lst):
#     new_lst = []
#     for i in lst:
#         if i not in new_lst:
#             new_lst.append(i)
#     return new_lst[:-1]
#
# def lstt(w):
#     while w != '':
#         w = input('enter the word: ')
#         ml.append(w)
#     return words(ml)
#
# ml = []
# w = input('enter the word: ')
# ml.append(w)
# print(lstt(w))



'''ex2'''
'''Գրեք ֆունկցիա, որը կվերադարձնի տվյալ թվի բոլոր բաժանարարների ցանկը: 
Այդ թիվը պետք է փոխանցվի ֆունկցիային որպես արգումենտ: Ֆունկցիայի արդյունքը կլինի թվի բաժանարարների ցուցակը:'''
# def div(n):
#     return [i for i in range(1, n) if n % i == 0]
#
# number = int(input("enter the number: "))
# print(div(number))

'''ex3'''
'''n ամբողջ թիվը կոչվում է կատարյալ, եթե նրա բոլոր բաժանարարների գումարը (բացի իրենից) հավասար է n-ին:
Գրել ֆունկցիա՝ որոշելու համար, թե արդյոք տվյալ թիվը կատարյալ է:Ֆունկցիան կվերցնի մեկ պարամետր որպես մուտք 
և կվերադարձնի True, եթե դա կատարյալ թիվ է, և False՝ հակառակ դեպքում:'''
# def div(n):
#     return sum([i for i in range(1, n) if n % i == 0]) == n
# number = int(input("Enter the number please: "))
# print(div(number))

'''ex4'''
'''
Գրել zip(data1, data2) ֆունկցիա, 
որը կվերադարձնի նոր լիստ, հետևյալ տեսքով [ [data1[0], data2[0]], [data1[1], data2[1]], … [data1[n - 1], data2[n - 1] ], 
որտեղ n-ը data1-ի և data2-ի երկարությունն է։
'''
# def zip(data1, data2):
#
#     if len(data1) == len(data2):
#         ziplst = []
#
#         for i in range(len(data1)):
#             ziplst.append([data1[i], data2[i]])
#
#         return ziplst
#     else:
#         return 'Lists are not equal'
#
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# print(f'Zip list: {zip(list1, list2)}')



'''ex5'''
'''Անգլերեն արտահայտություն «Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?»:
Պալինդրոմ նախադասություն է, քանի որ եթե այն կարդաս բառ առ բառ՝ անտեսելով կետադրական նշաններն ու մեծատառերը, երկու ուղղությամբ էլ նույնը կլինի։
Անգլերեն palindromes բառի օրինակներ են՝ «Herb the sage eats sage, the herb» և «Information school graduate seeks graduate school information»: 
Գրեք ծրագիր, որը կստանա օգտատիրոջից տողը և կտեղեկացնի, եթե դա բանավոր պալինդրոմ է: Հիշեք, որ արդյունքը հաշվելիս պետք է անտեսել կետադրական նշանները:
'''
# def is_symbols(sentence):
#
#     symbols = ',.!@#$%^&*()?'
#     mstr = sentence
#     for i in mstr:
#        if i in symbols:
#            mstr = mstr.replace(i, '')
#     return mstr
#
# def is_palindrom(sentence):
#
#     string = is_symbols(sentence)
#     string = string.title()
#     mstr = string.split(' ')
#     rev_string = mstr[::-1]
#
#     if mstr == rev_string:
#         return "the string is palindrom"
#     return "the string is not palindrom"
#
# sentence = input("Enter your sentence: ")
# print(is_palindrom(sentence))



'''ex6'''
'''Գրեք ծրագիր, որը օգտատիրոջից կստանա թվեր, մինչև բաց կթողնվի մուտքագրումը: 
Նախ, մուտքագրված թվերի միջին արժեքը պետք է ցուցադրվի էկրանին, որից հետո, 
մեկը մյուսի հետևից, անհրաժեշտ է ցուցադրել թվերի ցանկը միջինից ցածր, դրան 
հավասար (եթե առկա է) և միջինից բարձր:'''

# def numbers_list():
#
#     num_lst = []
#     number = input("Please enter the number: ")
#     num_lst.append(int(number))
#
#     while number != '':
#         number = input("Please enter the number: ")
#         if number != '':
#             num_lst.append(int(number))
#
#     return average(num_lst)
#
# def average(lst):
#
#     av = sum(lst) / len(lst)
#     return f'average is: {av}\nthe numbers who is < average: {[i for i in lst if i < av ]}\nthe numbers who equal are: {[i for i in lst if i == av ]} \
#            \nthe numbers who > average are: {[i for i in lst if i > av]}'
#
# print(numbers_list())



'''ex7'''
'''Գլխավոր մրցանակը շահելու համար վիճակախաղի տոմսի վեց համարները պետք է համընկնեն խաղարկության ժամանակ պատահականության սկզբունքով
խաղարկված վեց թվերի հետ՝ 1-ից 49 միջակայքում: Գրեք ծրագիր, որը պատահականորեն կընտրի ձեր տոմսի համար վեց թիվ: Համոզվեք, որ այդ թվերի մեջ կրկնվող թվեր չկան:
Ցուցադրել տոմսի թվերը էկրանին աճման կարգով:'''

# import random
# def rand_numbers():
#      lst = []
#      for i in range(6):
#          rand_num = random.randint(1, 49)
#          lst.append(rand_num)
#      return check_duplicate(lst)
#
# def check_duplicate(lst):
#     lst = sorted(lst)
#     set_lst = set(lst)
#     while len(lst) != len(set_lst):
#         return rand_numbers()
#     return f'your password is: {lst}'
#
# print(rand_numbers())


'''ex8'''
'''Գրեք ֆունկցիա, որը ցույց է տալիս արդյոք իրեն տրված ցանկը որպես պարամետր դասակարգված է (աճման կամ նվազման կարգով): 
Ֆունկցիան պետք է վերադարձնի True, եթե ցուցակը դասակարգված է, իսկ հակառակ դեպքում՝ False: Հիմնական ծրագրում օգտատիրոջից ստացեք
 թվերի հաջորդականություն ցուցակի համար, այնուհետև տպել հաղորդագրություն՝ ասելով, թե արդյոք այս ցուցակը ի սկզբանե դասակարգված է:'''

# def check(lst):
#
#     lst = lst.split(' ')
#     i = 0
#     new_lst = sorted(lst)
#     print('list must be: ', new_lst)
#     return lst == new_lst or lst == new_lst[::-1]
#
# lst = input("Enter your list's number with space: ")
# print(check(lst))

'''ex9'''
'''Տարրերի ենթաբազմություն կամ ենթացանկ համարվում է այն ցուցակը, որն ավելի մեծ ցուցակի մաս է: Ենթացանկը կարող է պարունակել մեկ տարր, մի քանի տարրեր կամ դատարկ լինել: 
Գրել is_sublist ֆունկցիա, որը որոշում է, թե արդյոք մի ցուցակը մյուսի ենթացանկ է: 
Ֆունկցիան պետք է ստանա երկու ցուցակ՝  larger և smaller:Ֆունկցիան պետք է վերադարձնի True միայն այն դեպքում, եթե smaller ցուցակը larger֊ի ենթացանկ է:
'''

# def is_sublist(l, s):
#
#     is_sub = False
#     if s == []:
#         is_sub = True
#     elif s == l:
#         is_sub = True
#     elif len(s) > len(l):
#         is_sub = False
#
#     else:
#         for i in range(len(l)):
#             if l[i] == s[0]:
#                 n = 1
#                 while (n < len(s)) and (l[i + n] == s[n]):
#                     n += 1
#
#                 if n == len(s):
#                     is_sub = True
#
#     return is_sub
#
#
# larger = [21, 34, 67, 34]
# smaller = []
# print(is_sublist(larger, smaller))














