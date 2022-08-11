# var1 =9 # var1 is in the global namespace

# def func():
#      var2=99 # var2 is in the local namespace

#      def inner_func():
#           var3=44
#           # var3 is in the nested local
#           # namespace


# count=1

# def some_method():
#      global count
#      count+=1
#      print(count)

# some_method()


# a=10
# print(a)
# _=10
# b=10
# print(id(a))
# print(id(_))

# Python program showing
# a scope of object
j = 1
while(j<= 5):
     print(j)
     j = j + 1
 
# def some_func():
#     print("Inside some_func")
#     def some_inner_func():
#         var = 10
#         print("Inside inner function, value of var:",var)
#     some_inner_func()
#     print("Try printing var from outer function: ",var)
# some_func()


# program illustrates the use of docstrings
 
def helloWorld():
  """ This program prints out hello world """ #This is a docstring comment
  print("Hello World")

helloWorld()
print(helloWorld.__doc__)



import math

print(math.__doc__)