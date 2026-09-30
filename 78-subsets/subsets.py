class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def getSubset(index, current):
            #base condition
            if index == len(nums):
                ans.append(current[:])
                return

            #Dont take condition in recursion
            getSubset(index + 1, current)

            #Take condition , make sure addition is done first in current
            current.append(nums[index])
            getSubset(index + 1, current)

            #Backtracking to previous deciesion state
            current.pop()

        #first call
        getSubset(0, [])
        return ans 
