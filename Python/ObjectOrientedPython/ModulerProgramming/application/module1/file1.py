class ArithmeticOperations:
    def __init__(self) -> None:
        self.sum = 0
    def get_sum(self, num1, num2):
        self.sum = num1+num2;
        return self.sum
    



class PrintData:
    def __init__(self) -> None:
        self.data=""
    
    def print_data(self,data):
        self.data = data
        return self.data