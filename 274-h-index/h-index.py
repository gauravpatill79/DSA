class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        freq = [0] * (n + 1)
        #filling up the freq arr
        for citation in citations:
            if  citation >= n: #any no out of n will be added in last number
                freq[n] += 1
            else: 
                freq[citation] += 1

        papers = 0
        #i will check how many paper i have with h greater citations
        for h in range(n, -1 , -1):
            papers += freq[h]
            if papers >= h : #any time we find sum of paper > h we have the h index
                return h
        return 0

