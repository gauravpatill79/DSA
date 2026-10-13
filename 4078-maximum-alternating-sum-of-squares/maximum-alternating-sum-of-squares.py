class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        negativeSum = 0 
        positiveSum = 0

        for i in range(0, n//2) :
            negativeSum += nums[i] ** 2
        
        for i in range(n//2 , n):
            positiveSum += nums[i] ** 2

        return positiveSum - negativeSum