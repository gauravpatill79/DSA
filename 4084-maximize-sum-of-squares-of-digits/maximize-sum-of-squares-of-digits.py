class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        if sum > 9 * num: #the biggest possible digit sum is 9 * num
            return ""
    
        ans = []
        
        for _ in range(num): #every position from left to right
            digit = min(9, sum) # take as much as we can, at most 9
            ans.append(str(digit))
            sum  -= digit
        
        return "".join(ans) if sum == 0 else ""
