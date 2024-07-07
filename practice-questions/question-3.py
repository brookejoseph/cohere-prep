#creating a circle 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius 
    

class calulcator:
    def __init__(self, operation, number1, number2):
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
    
    def calculate(self):
        if self.operation == 'add':
            return self.number1 + self.number2 
        elif self.operation == 'subtract':
            return self.number1 - self.number2
        elif self.operation == 'multiply':
            return self.number1 * self.number2
        elif self.operatoin == 'divide':
            return self.number1 / self.number2
        else:
            return 0
        
