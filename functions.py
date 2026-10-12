# def Greet():
#     print("Hello Python")

# def Greet(name,city):
#     print("Hello "+name+" "+city)


# Greet("Khushi","Indori")
# Greet("Ritik","Indori")
# Greet("Chirag","Indori")



# def Sums(a):
#     i = 1
#     sum = 0
#     while(i <= a):
#         sum = sum + i
#         i += 1

#     print("The sum is",sum)


# Sums(40)


# def Sums(*nums):
#     sum=0
#     for i in nums:
#         sum+=i
#     return sum

# res = Sums(12,43,23,65,34,12)
# print(res)

# def Sums(*nums):
#     sum=0
#     for i in enumerate(nums):
#         sum+=i[1]
#         if i[0]==3:
#             break
#     return sum


# print(Sums(12,43,23,65,34,12))

# def Dummy(**args):
#     print(args)

# Dummy(name="Kalu",age=220,city="Indore")
# Dummy(name={"name": "Kalu"},age=220,city="Indore")


#Lambda function -> a short functions.
# Sum = lambda x,y : x+y

# s=Sum(45,55)
# print(s)


# a = 10

# declare a global variable
# def Dummy():
#     global a
#     a=a+5
#     print(a)

# Dummy()
# print(a)


# Docstring is used to describe about functions.
# def Dummy():
#     """This function is used to test how function works"""
#     print("Test")


# Dummy()



# Decorator Function

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())
