class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positiveArr = []
        negativeArr = []
        ans = []
        positiveIdx = negativeIdx = 0
        
        for ele in nums :
            if ele > 0 :
                positiveArr.append(ele)
            else:
                negativeArr.append(ele)
        n = len(positiveArr)    #since both arr are of same size
        for i in range(0, n):
            ans.append(positiveArr[positiveIdx])
            if positiveIdx < n:
                positiveIdx += 1
            ans.append(negativeArr[negativeIdx])
            if positiveIdx < n:
                negativeIdx += 1
        return ans

        