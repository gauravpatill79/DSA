class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or strs == None : return ""
        n = len(strs)
        for i in range(len(strs[0])):
            ch = strs[0][i]

            for j in range(1,n):
                if i == len(strs[j]) or strs[j][i] != ch :
                    return strs[0][:i]

        return strs[0]