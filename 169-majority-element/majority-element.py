class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        candidate = nums[0]
        freq = 1
        for i in range(n):
            if candidate == nums[i]:
                freq+=1
            else:
                freq-=1
            if freq == 0:
                candidate = nums[i]
                freq = 1
        return candidate