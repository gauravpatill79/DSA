import heapq 
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        pq = []
        freq = Counter(s)
        # Push into max-heap based on frequency 
        for ch , count in freq.items():
            heapq.heappush_max(pq, (count , ch))

        #get elements
        ans = []
        while pq :
            count , ch = heapq.heappop_max(pq)
            ans.append(ch * count)

        return ''.join(ans)


