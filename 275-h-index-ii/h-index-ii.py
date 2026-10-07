class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right - left) // 2
            baseCitationPaper = n - mid # means from this point till end all the paper are valid, among all try to find minimum among all valid paper
            if citations[mid] >=  baseCitationPaper:
                right = mid - 1
            else:
                left = mid + 1
        return  n - left #since from here all the valid paper starts so we return first idx