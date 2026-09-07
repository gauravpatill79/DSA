class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n != m : return False

        m1 = {}
        m2 = {}

        for i in range(n):
            a = s[i]
            b = t[i]

            if a in m1 and m1[a] != b:
                return False
            if b in m2 and m2[b] != a :
                return False

            m1[a] = b
            m2[b] = a

        return True