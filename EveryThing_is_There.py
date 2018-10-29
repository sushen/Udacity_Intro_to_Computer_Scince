#Lesson 5 Chapter 3


# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

########    1   #########
# Using Simple Logic from Alan Turin

# def biggest(a,b,c):
#     if a>=b:
#         if a>=c:
#             return a
#     if b>=a:
#         if b>=c:
#             return b
#     if c>=a:
#         if c>=b:
#             return c

########    2   #########
# Using Procedure and That How All Build in program Build

def bigger(a,b):
    if a>b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(bigger(a,b),c)

########   3  #########
# Bildin Function
# def biggest(a,b,c):
#     return max(a,b,c)

print (biggest(3, 6, 9))
# #>>> 9
#
print (biggest(6, 9, 3))
# #>>> 9
#
print(biggest(9, 3, 6))
# #>>> 9
#
print (biggest(3, 3, 9))
# #>>> 9
#
print (biggest(9, 3, 9))
# #>>> 9