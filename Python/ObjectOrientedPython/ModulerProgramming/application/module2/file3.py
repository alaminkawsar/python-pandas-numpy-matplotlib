#Remember one thing.. we need to go the current directory to run this folder.

import sys

#it syas go back first, then find moudule1
sys.path.insert(0,"..")
 
from module1.file1 import ArithmeticOperations
 
 
obj = ArithmeticOperations()
print(obj.get_sum(8,23))