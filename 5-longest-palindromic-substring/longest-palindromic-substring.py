class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        start = 0
        maxLen = 1

        def expand(left, right):
            nonlocal start, maxLen

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    start = left

                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)       # odd
            expand(i, i + 1)   # even

        return s[start:start + maxLen]