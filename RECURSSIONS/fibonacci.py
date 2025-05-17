class Fib:
    def fibonacci(self, n : int ) -> int :
        if n == 0 :
            return 0
        if n == 1:
            return 1
        
        return (self.fibonacci(n-1 )+ self.fibonacci(n-2))
    
    
fibo = Fib()
print(fibo.fibonacci(5))
    
        
        
        