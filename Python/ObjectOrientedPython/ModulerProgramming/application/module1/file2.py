import file1
from file1 import ArithmeticOperations

obj1 = file1.ArithmeticOperations()
c = obj1.get_sum(3,8)
print(c)

obj2 = ArithmeticOperations()
print(obj2.get_sum(15,20))
