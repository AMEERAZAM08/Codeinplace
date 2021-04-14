
x = 5  #x holding integer number 
y = "John" # y holding string of len 4
print(x)
print(y)
size= len(y)  # is for finding the lenght of string in len 
              # input must be string 
              #to check the type of that input using simple func 
#print(type(x)) # ouput is int class 
#print(type(y)) # output is string class 


#python execution is done in line by line 
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting    If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


#Get the Type You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

#same Quotation
x = "John"
# is the same as
x = 'John'

#look twice then judge
a = 4
A = "Sally"
#A will not overwrite a

#var name 
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#not valid name 
#2myvar = "John"
#my-var = "John"
#my var = "John"

#assign multiple value
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)


#list is use we will see in next upcoming replit
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)

print(y)

print(z)

#output var 
x = "awesome"
print("Python is " + x)


x = "Python is "
y = "awesome"
z =  x + y
print(z)


x = 5
y = 10
print(x + y)


#If you try to combine a string and a number, Python will give you an error:

#Example
#x = 5
#y = "John"
#print(x + y)
#type of var must be same 