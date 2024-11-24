class Calculator:
    
    def add(self, a, b):
        if type(a) != int or type(b) != int:
            return "Please enter only integer"
        return a + b

    def subtract(self, a, b):
        if type(a) != int or type(b) != int:
            return "Please enter only integer"
        return a - b

    def multiply(self, a, b):
        if type(a) != int or type(b) != int:
            return "Please enter only integer"
        result = 0
        for i in range(abs(b)):
            result = self.add(result, a)
        if (b < 0):
            return -result
        return result

    def divide(self, a, b):
        if type(a) != int or type(b) != int:
            return "Please enter only integer"
        if b == 0:
            return "Divided by zero"
        
        negative = (a < 0) != (b < 0)  
        a, b = abs(a), abs(b)
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        if negative:
            result = -result
        
        return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))