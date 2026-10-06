class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack = []
        # n = len(s)
        # count = 0
        # for ch in s:
        #     if ch == '(':
        #         stack.append(ch)
        #     else:
        #         if stack:
        #             stack.pop()
        #         else:
        #             count += 1
                
        # return count + len(stack)
        unmatchedCount = 0
        ans = 0
        for ch in s :
            if ch == "(":
                unmatchedCount +=1
            else:
                if unmatchedCount > 0:
                    unmatchedCount -=1
                else:
                    ans += 1
        return ans + unmatchedCount

