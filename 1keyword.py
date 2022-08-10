# from curses import nonl
import keyword
from pickle import TRUE
from turtle import pen
import math as gfg

# print("the keyword is : ")
# print(keyword.kwlist)


# print(False==0)


# print(True==1)


# print(True+False+True)
# print(True+True+True)
# print(False+False+False)


# print(None == 0)
# print(None == [])

# print(True or False)
# print(True and False)



# print(not False)

# if 'd' in "geeksforgeeks":
#      print("s in the word")
# else:
#      print("s not in the word")




# for i in "Geeeksforgeeks":
#      print(i,end=" ")


# print("\r")

# print('s' is 's')


# print({} is {})


# for i in range(10):
#      print(i, end=" ")
#      if i==5:
#           break



# print()



# i=0
# while i<10:
#      if i==6:
#           i+=1
#           continue
#      else:
#           print(i,end=" ")

#      i+=1


# i = 20
# if (i == 10):
#     print ("i is 10")
# elif (i == 20):
#     print ("i is 20")
# else:
#     print ("i is not present")


# def fun():
#      print("Inside function")


# fun()



# class dog:
#      attr1="mammal"
#      attr2="dog"

#      def fun(self):
#           print("I am a",self.attr1)
#           print("I am a",self.attr2)


# rodger = dog()

# print(rodger.attr2)


# rodger.fun()




# print(gfg.factorial(5))

# n = 10
# for i in range(n):
      
# # pass can be used as placeholder
# # when code is to added later
# pass


# g = lambda x: x*x*x

# print(g(7))


# # import keyword
# import math
# print(math.factorial(10))
  
# # from keyword
# from math import factorial
# print(factorial(10))

# initializing number
# a = 4
# b = 0
  
# # No exception Exception raised in try block
# try:
#     k = a//b # raises divide by zero exception.
#     print(k)
  
# # handles zerodivision exception
# except ZeroDivisionError:
#     print("Can't divide by zero")
  
# finally:
#     # this block is always executed
#     # regardless of exception generation.
#     print('This is always executed')
  
# # assert Keyword  
# # using assert to check for 0
# print ("The value of a / b is : ")
# assert b != 0, "Divide by 0 error"
# print (a / b)


# my_variable1 = 20
# my_variable2 = "GeeksForGeeks"
  
# # check if my_variable1 and my_variable2 exists
# print(my_variable1)
# print(my_variable2)
  
# # delete both the variables
# del my_variable1
# del my_variable2
  
# # check if my_variable1 and my_variable2 exists
# print(my_variable1)
# print(my_variable2)







a=15
b=10


def add():
     c=a+b
     print(c)


add()



def fun():
     var1=10
     def gun():
          # nonlocal is a keyword
          nonlocal var1
          var1=var1+10
          print(var1)
     gun()
fun()