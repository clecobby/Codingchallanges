class Factorial:
    def getfactorial(self,n : int ):
         print(f"Entering with n = {n}")
         if n == 0:
             print("Hit base case, returning 1")
             return 1
         else:
             result = n * self.getfactorial(n-1)
             print(f"Unwinding: {n} * factorial({n-1}) = {result}")
             return result
    
factorial = Factorial()
print(f"Final result: {factorial.getfactorial(100)}")        
        
    
