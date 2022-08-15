# Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.


# print("Akash Das")

# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ")
# print(String1)


# String1 = "I'm a Geek"
# print("\nString with the use of Double Quotes: ")
# print(String1)


# String1 = '''I'm a Geek and I live in a world of "Geeks"'''
# print("\nString with the use of Triple Quotes: ")
# print(String1)


# String1 = '''Geeks
#             For
#             Life'''
# print("\nCreating a multiline String: ")
# print(String1)


# str = "GeeksforGeeks"

# print(str[0:7])

# print("\nLast character of String is: ")
# print(str[-1])

# print(str[::-1])

# gfg = "geeksforgeeks"

# gfg = "".join(reversed(gfg))


# print(gfg)

# # Python Program to Update
# # character of a String

# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1)

# # Updating a character of the String
# ## As python strings are immutable, they don't support item updation directly
# ### there are following two ways
# #1
# list1 = list(String1)
# list1[2] = 'p'
# String2 = ''.join(list1)
# print("\nUpdating character at 2nd Index: ")
# print(String2)

# #2
# String3 = String1[0:2] + 'p' + String1[3:]
# print(String3)



# # Deletion of a character: 

# str = "Hello I'm Ak"
# print(str)

# str2 = str[0:2] + str[3:]
# print(str2)





# # Deleting Entire String:
# s = "AKash Das"
# print(s)

# del s

# print(s)



str = "Im {}".format('AK')
print(str)

str = "Im {2} {0} {1}".format('AK','ak','Y')
print(str)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)














