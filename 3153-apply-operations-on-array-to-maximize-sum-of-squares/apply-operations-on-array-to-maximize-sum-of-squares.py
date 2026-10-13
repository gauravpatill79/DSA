class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        BITS = 30 # nums[i] <= 10^9 < 2^30
        count = [0] * BITS
        #filling the count array
        for num in nums:
            for b in range(BITS):
                if (num >> b) & 1 :
                    count[b] += 1
        
        res = 0
        #getting the numbers using the count stored in the counts arr
        for _ in range(k):
            curr = 0 
            for b in range(BITS):
                if count[b] > 0:
                    count[b] -= 1
                    curr |= (1 << b)

            res = (res + curr * curr ) % MOD
        
        return res

