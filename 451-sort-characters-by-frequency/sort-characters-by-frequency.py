import heapq
from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        pq = []
        freq = Counter(s)

        #pushing elements : multiply by -1 to make it large 
        for ch, count in freq.items() :
            heapq.heappush(pq, (-count , ch))
        
        ans = []
        while pq:
            count , ch = heapq.heappop(pq)
            ans.append(ch * (-count))
        
        return ''.join(ans)
