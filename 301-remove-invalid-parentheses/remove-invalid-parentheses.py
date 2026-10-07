class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = set()
        minCount = float('inf')

        def getParantheses (index, balance, removedCount, path):
            nonlocal minCount
            if removedCount > minCount:
                return
            n = len(s)
            #base condition
            if index == n :
                if balance == 0:
                    if removedCount < minCount :
                        minCount = removedCount
                        ans.clear()
                        ans.add(path)
                    elif removedCount == minCount :
                        ans.add(path)

                return 
            
            ch = s[index]

            if ch.isalpha():
                getParantheses(index + 1 , balance , removedCount, path + ch)
    
            elif ch == "(":
                #keep
                getParantheses(index + 1 , balance + 1, removedCount, path + ch)
                #remove
                getParantheses(index + 1 , balance , removedCount + 1, path )
                
            else:
                #keep
                if balance > 0:
                    getParantheses(index + 1 , balance - 1 , removedCount, path + ch)
                #remove
                getParantheses(index + 1 , balance  , removedCount + 1, path )

        getParantheses(0, 0, 0, "")
        return list(ans)