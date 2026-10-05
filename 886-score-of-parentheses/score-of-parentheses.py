class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [] 
        #looping over the stack
        for ch in s:
            if ch == "(" :
                stack.append(0)
            else :
                ans = stack.pop()
                if ans == 0:
                     score = 1
                else:
                    score = 2 * ans 

                if stack :
                    stack[-1] += score
                else:
                    stack.append(score)

        return stack[-1]


