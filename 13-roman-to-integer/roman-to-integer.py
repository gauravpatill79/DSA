class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        val = 0
        for i in range(n):
            curr = mp[s[i]]
            next_val = mp[s[i+1]] if i + 1 < n else 0

            if curr < next_val :
                val -= curr
            else:
                val += curr
        return val
