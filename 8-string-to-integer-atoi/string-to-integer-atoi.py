class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        #remove whitespace
        while i < n and s[i] ==' ':
            i += 1
        
        if i == n :
            return 0
        
        #check for sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = 1 if s[i] == '+' else -1
            i+= 1
        
        #generate nums
        num = 0

        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))

            if sign * num > 2**31-1:
                return 2**31-1
            if sign * num < -2**31:
                return -2**31

            i+=1
        return sign * num
            