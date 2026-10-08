class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = 0
        ans = nums[0]
        for el in nums:
            max_sum += el
            ans = max(ans, max_sum)
            if max_sum < 0:
                max_sum = 0
                
        return ans