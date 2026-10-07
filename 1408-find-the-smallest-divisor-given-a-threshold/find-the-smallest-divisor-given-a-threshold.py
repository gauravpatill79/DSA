class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right :
            mid = left + (right - left) // 2
            total = 0

            #checking the contribution of the element with given mid
            for currNumber in nums:
                total += (currNumber + mid - 1) // mid
                if total > threshold:
                    break
                
            if total <= threshold:
                right = mid - 1
            else:
                left = mid + 1    #find higher mid to get sum < threshold 

        return left