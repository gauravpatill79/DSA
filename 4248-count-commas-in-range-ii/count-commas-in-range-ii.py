class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1000
        c = 1
        ans = 0
        while base <= n:
            next_val = base * 1000-1
            if next_val > n :
                next_val = n 
            ans += (next_val - base + 1) * c

            base *= 1000
            c += 1
        return ans