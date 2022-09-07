# print values

# Print a integer value
my_int = 4
print(my_int)
# Print a float value
my_float = 4.6
print(my_float)
# Print a String
my_string = "Hello World"
print(my_string)
# Print a boolean value
my_bool = not True
print(my_bool)
# Print a None value
x = None
print(x)
# Print a f-string containing all previous values in one line i.e 1, 1.0, "hello" ..
print(f"{my_int}, {my_float}, {my_string}, {my_bool}, {x}")

#Create a program that uses `input` and type conversion
#Input a string and assign it to a variable, then print the variable
my_new_string = input("What's your name?: ")
print(my_new_string)
# Input a number and assign it to a variable, print the value doubled
value = int(input("Double the value: "))
print(value * 2)
#Input a string i.e `hello` and assign it to a variable, print the string repeated `hellohello`
new_string = input("Greetings: ")
print(new_string * 2)
#Input a float and assign it to a variable, print the value divided by 3.5
new_value = float(input("Divided the value by 3.5: "))
print(new_value / 3.5)






