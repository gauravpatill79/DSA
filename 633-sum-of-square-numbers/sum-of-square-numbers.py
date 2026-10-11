class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ans = 0
        left = 0
        right = int(c ** 0.5) #getting the square root as the upper limit so that square does not go above c
        while left <= right :
            prod = left * left + right * right
            if prod == c :
                return True
            elif prod < c :
                left += 1
            else:
                right -= 1
        return False



        