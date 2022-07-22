import sys
sys.path.insert(0,"..")
 
from module1.file1 import ArithmeticOperations
 
 
obj = ArithmeticOperations()
print(obj.get_sum(8,23))