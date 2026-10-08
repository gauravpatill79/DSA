class Solution:
    def myPow(self, x: float, n: int) -> float:
        #base condition
        if n == 0:
            return 1

        if n < 0 :
            return 1 / self.myPow(x, -n)
        
        
        #even case -> we can half the exponent and square -> same result
        if n % 2 == 0:
            half = self.myPow(x , n // 2)
            return half * half #sqauring
        
        
        return x * self.myPow(x, n-1)