class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        max_depth = 0
        ans = 0
        for ch in s:
            if ch == "(":
                max_depth += 1
                ans = max(max_depth , ans)
            elif ch == ')':
                    max_depth -= 1
        return ans

