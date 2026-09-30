class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isNum = self.pow(n)
        return isNum

    def pow(self, n):

        if n == 1 : 
            return True

        if n <= 0 or  n % 2 != 0 :
            return False
        
        return self.pow(n // 2)


