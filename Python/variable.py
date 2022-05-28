#variable in different line

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value assign in multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

#python allows you to unpack variable
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# global variable

def myfunc():
  print("Python is " + x)

myfunc()

#using global keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)