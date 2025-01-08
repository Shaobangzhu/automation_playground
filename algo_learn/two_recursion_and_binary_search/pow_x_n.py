class PowXN: 
    def myPow(self, x: float, n: int) -> float:
            if n < 0:
                return 1.0 / self.pow(x, -n)
            return self.pow(x, n)
        
    def pow(self, x: float, n: int) -> float:
            if n == 0:
                return 1.0
            
            tmp = self.pow(x, n//2)
            
            if n % 2 == 0:
                return tmp * tmp
            else:
                return tmp * tmp * x

    def __init__(self, x: float, n: int):
        self.x = x
        self.n = n
        # Call the myPow method using self
        print(self.myPow(x,n))
        
# Instantiate the class with arguments
pow_calculation = PowXN(2.00000, 10)