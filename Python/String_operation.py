#string method link when necessary: https://www.w3schools.com/python/python_strings_methods.asp

#multiple string uses three double/single qoutos.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#slicing string
#starting with zero
b = "Hello, World!"
print(b[2:5])

#slice from the start
b = "Hello, World!"
print(b[:5])

#slice to the end
b = "Hello, World!"
print(b[2:])

#negative indexing
b = "Hello, World!"
print(b[-5:-2])

#upper
a = "Hello, World!"
print(a.upper())

#lower
a = "Hello, World!"
print(a.lower())

#remove white space from the beggining and the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#split(",") split the string by ',' character and make a list
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#search a pattern is have or not
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#format the value where {} occurs
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

#make double quotation using \"write string\"
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

