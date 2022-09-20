# Exercise 1 raise #upptäckt fel och hantera den
#1. 
# x = 1
# if not type(x) is float:
#     raise TypeError("This is not a float")

# def is_float(value):
#     if not isintance(value, float): #isinstance (är värdet en float) returns True if the specified object is of the specified type, otherwise False.
#         raise TypeError("Value is not a float")
#Exercise 2 input validation
#1.2.3.
def int_input():
    try:
        return int(input("Write a integer: "))
    except:
            print("Sorry, not an int")
            return int_input()


def even_input():
    number = int_input()
    if not number % 2:
        raise Exception('Even numbers is not allowed')
    return number


even_input()
# def int_input(text):
#     number = None
#     while True:
#         try:
#             number = int(input(text)) 
#             break
#         except ValueError:
#             print("Sorry, not an int")
        
#     return number

# my_number = int_input("Enter a number: ")

#4. raise Exception("Even number is not allowed")

# def int_input(text):
#     number = None
#     while True:
#         try:
#             number = int(input(text)) 
#             assert number % 2 == 0
#         except ValueError:
#             print("Sorry, not an int")
#         except:
#             raise("Even number is not allowed")
        
#     return number

# my_number = int_input("Enter a number: ")

