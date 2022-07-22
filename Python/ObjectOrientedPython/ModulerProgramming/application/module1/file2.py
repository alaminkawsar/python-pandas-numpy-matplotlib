import file1
from file1 import ArithmeticOperations

obj1 = file1.ArithmeticOperations()
c = obj1.get_sum(3,8)
print(c)

#another way
obj2 = ArithmeticOperations()
print(obj2.get_sum(15,20))



#import all of classes
from file1 import*
obj3 = ArithmeticOperations()
print(obj3.get_sum(10,10))

obj4 = PrintData()
print(obj4.print_data("Accessing Another class from file2"))
