class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #base condition
        if n == 0 :
            return 1

        if n < 0 :  # doing so that negative exponent gets converted to postive
            return 1 / self.myPow( x , -n)

        #even exponent
        if n % 2 == 0:
            #we will half the exponent and square the base
            half = self.myPow(x, n // 2)
            return half * half

        #odd exponent -> we can remove one x and make it even , x X x^ x-1

        return x * self.myPow(x, n- 1)



        