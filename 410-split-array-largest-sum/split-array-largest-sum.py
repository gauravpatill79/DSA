class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right :
            mid = left + (right - left) // 2
            largestSum = 0
            splitCount = 1

            for firstMaxiSum in nums:
                if largestSum + firstMaxiSum <= mid:
                    largestSum += firstMaxiSum
                else:
                    splitCount += 1
                    largestSum = firstMaxiSum

            if splitCount <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans 
                    
                
