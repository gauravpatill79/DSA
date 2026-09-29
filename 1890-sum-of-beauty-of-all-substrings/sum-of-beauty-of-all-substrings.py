class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26 #since we have only 26 chars
            for j in range( i , n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                maxFreq = 0
                minFreq = float('inf')

                for f in freq:
                    if f > 0:
                        maxFreq = max(maxFreq, f)
                        minFreq = min(minFreq, f)

                ans += maxFreq - minFreq

        return ans
