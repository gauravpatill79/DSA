class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        self.getParenthesis("", 0, 0, n, ans )
        return ans

    def getParenthesis(self, current , openCount, closeCount, n, ans):
        #base condition 
        if openCount == n and closeCount == n :
            ans.append(current)
            return ans

        #Add '('
        if openCount < n :
            self.getParenthesis(current + "(", openCount + 1 , closeCount , n , ans)

        #Add ')'
        if closeCount < openCount :
            self.getParenthesis(current + ")" , openCount , closeCount + 1 , n , ans)