class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        n = len(arr)
        left = 0
        right = n-1
        while left <= right:
            arr[left] , arr[right] = arr[right] , arr[left]
            
            left+=1
            right -=1
        return " ".join(arr)