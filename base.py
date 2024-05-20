
# edibles = ["отбивные", "яйца", "орехи"]
#
#
# for food in edibles:
#    if food == "пельмени":
#         print("Я не ем пельмени!")
#        break
#    print("Отлично, вкусные " + food)
# else:
#  print("Хорошо, что не было пельменей!")
# print("Ужин окончен.")


# data = {1: 'HI', 2 : 'Akim', 3: 'Love', 4:'Gilyana'}
# for i in data.values():
#    print (i)


# i = 0
# while i < 11: # i = 1
#    print(i) # 1
#    i = i + 1 # i = 1 + 1 = 2
#
# while условное выражение >< == !=
# 2 < 4 и
#
# a = 2345
# print (a % 10 == 6) # 5
# print(a //10) # 2345 // 10 = 234, 5
#
# a = 2345
# print(a % 100) # 23,45 --> 45


# x = 5
# if x > 0:
#    print("x положительное число")
# elif x < 0:
#    print("x отрицательное число")
# else:
#    print("x равен 0")


# x = 0
# if x > 0:
#     print("x положительное число")
# elif x < 0:
#    print("x отрицательное число")
# else:
#     print("x равень нулю")


# my_list = [1, 2, 3, 4, 5]
#
# for item in my_list:
#     my_list.append(item)
#     print(item*2)


# my_list = [1, 2, 3, 4, 5]
# new_lst = []
# for item in my_list:
#      print(item*2)


# my_range = range (5)
#
# for item in my_range:
#     print(item)


# 29.02.2024 Функция как тип


# def say_hello():
#     print('hello')
# def say_goobye():
#     print('good bye')
# message = say_hello
# message()
# message = say_goobye
# message()


# def sum(a,b):
#     return a + b
# def mult (a,b):
#     return a * b
# operation = sum
# result = operation (5,6)
# print(result)
#
# operation = mult
# print(operation(5,6))

# функции == методы = глагол

#def say_hello(a,b):
 #   return a + b
#print(say_hello(3,5))

# print() int () float () - фунцкии pythone

# рекурсия
# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x+1)
#         print(x)
# rec(1)


# факториал числа (рекурсия)

# def fact (x):
#     if x == 1:
#         return 1
#     return fact  (x-1)*x
# print(fact(3))

#def check(n):
   # if (n < 2):
  #      return (n % 2 == 0)
 #   return  check(n-2)
#n = int(input('введите число'))
#if (check(n) == True):
 #   print('число  четное')
#else:
  #  print('число нечетное')

# итераторы и генераторы