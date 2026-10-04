class Solution:
    def checkValidString(self, s: str) -> bool:
        firstStack = []
        secondStack = []

        if not firstStack and s[0] == ")":
            return False
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch == "(":
                firstStack.append(i)
            elif ch == "*":
                secondStack.append(i)
            else:
                if firstStack:
                    firstStack.pop()
                elif secondStack:
                    secondStack.pop()

                else:
                    return False
                   
         #for some of remaining brackets
        while firstStack and secondStack:
            if firstStack[-1] < secondStack[-1]:
                firstStack.pop()
                secondStack.pop()
            else:
                return False
        return not firstStack          



#s = "(*))("