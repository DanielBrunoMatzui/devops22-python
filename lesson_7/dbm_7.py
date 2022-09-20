# Exercise 1 Functions
#1.(1. + 2.) pass is a null statement. The interpreter does not ignore a pass statement,
#  but nothing happens and the statement results into no operation.
def do_nothing():
    pass

do_nothing() #anrop inom tom ()

#2. (1.)
def string():
    print("hello world")

string()
#(2.)
def one():
    print(1 == 1.0)

one()

#(3.)
import string
def reversed_alphabet():
    print(string.ascii_lowercase[::-1])

reversed_alphabet()
# var_1 = hello()
# var_2 = ones()
# var_3 = reversed_alphabet()

# print(f"{var_1} {var_2} {var_3}")

#3. (1.)
def my_function(name):
    print("hello " + name)

my_function("Daniel")

# (2.)
def my_function(word):
    print(word.upper())

my_function("daniel")

#(3.) ?????
def my_function():
    for i in range(1, 14):
        print(i)

def number_printer(stop):
    print(list(range(1, stop)))

# print(f" {my_function()} {number_printer(stop)}")

#Exercise 2 Default arguments
#1. 
def default_number_printer(start=1, stop=11):
    print(list(range(start, stop)))

default_number_printer(start=1, stop=11)

#2. ????????
def rev_string(word, reverse=False):
       if reverse:
          word = word[::-1]
          print(word)

# rev_string("hello")
# rev_string("hello", reverse=True)

#Exercise 3 Return
#1.
def get_int():
    return 5

print(get_int())

#2. ???
def get_tup(x, y):
    return x, y

# print(get_tup(x, y))

#3.
def get_bool():
    return False

print(get_bool())

#4.
def get_float():
    return 2.5

print(get_float())

#5.
def fullname(firstname, lastname):
    return f'{firstname} {lastname}'

print(fullname("Dan", "Svensson"))
#6. 
def area(l, b):
    return l*b

print(area(4, 6))

#7.
def sum_list(values):
    return sum(values)

sum_list = 1 + 2 + 3 + 6
print(sum_list)

#8. use return!!!!!!
def copy(word, repeat):
    for r in range(repeat):
        print(word)

copy("hello", 3)


