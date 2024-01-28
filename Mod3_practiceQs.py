#Q1: create variable and assign it the integer value of 15
var1 = 15
print(type(var1))

#Q2:create avariable and assign it the float value of 6.36272
var2 = 6.36272
print(type(var2))

#Q3:create a variable and assign it a Boolean, then print
var3 = 16 > 5
print(var3)

#Q4:create 3 variables, all strings, and concatenate them
string1 = "You"
string2 = "got"
string3 = "this Insha'allah"

print(string1 + string2 + string3)

a, b = 5, 10

print(a,b)

print(string1 + " " + string2 + " " + string3)

numbers = {"First Num": ' 1', "Second Num": ' 2', "Third Num": ' 3'}
for key, value in numbers.items():
    print(F"Key {key} has a value of{value}")

Name = "Omar"
age = "47"
print(F"His name is {Name} and he is {age} years old")