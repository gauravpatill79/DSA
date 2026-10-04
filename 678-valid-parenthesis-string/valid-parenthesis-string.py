class Solution:
    def checkValidString(self, s: str) -> bool:
        # firstStack = []
        # secondStack = []

        # if not firstStack and s[0] == ")":
        #     return False
        # n = len(s)
        # for i in range(n):
        #     ch = s[i]
        #     if ch == "(":
        #         firstStack.append(i)
        #     elif ch == "*":
        #         secondStack.append(i)
        #     else:
        #         if firstStack:
        #             firstStack.pop()
        #         elif secondStack:
        #             secondStack.pop()

        #         else:
        #             return False
                   
        #  #for some of remaining brackets
        # while firstStack and secondStack:
        #     if firstStack[-1] < secondStack[-1]:
        #         firstStack.pop()
        #         secondStack.pop()
        #     else:
        #         return False
        # return not firstStack          

        #O(1) optimized solution

        minOpen = 0
        maxOpen = 0
        for ch in s :
            if ch == "(":
                minOpen += 1
                maxOpen += 1
            elif ch == ")":
                minOpen -= 1
                maxOpen -= 1
            else: # '*" 
                minOpen -= 1     # Treat '*' as ')' for minimum possible '('
                maxOpen += 1     # Treat '*' as '(' for maximum possible '('

            minOpen = max(0, minOpen) # We cannot have negative unmatched '('
            if maxOpen < 0 :
                return False

        return minOpen == 0
                
