class Solution:
    def countGoodNumbers(self, n: int) -> int:
         MOD = 10 ** 9 + 7

         evenCount = (n + 1) // 2
         oddCount = n // 2

         evenWays = pow(5, evenCount, MOD)
         oddWays = pow(4, oddCount, MOD)

         return (evenWays * oddWays ) % MOD
