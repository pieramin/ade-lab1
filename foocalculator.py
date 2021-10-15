import calculator as calc

class foocalculator:
    def __init__(self):
        pass

    def sum(self,m,n):
        return calc.sum(m,n)

    def divide(self,m,n):
        return calc.divide(m,n)

cal = foocalculator()
print(cal.sum(4,5))
print(cal.sum(5+6))