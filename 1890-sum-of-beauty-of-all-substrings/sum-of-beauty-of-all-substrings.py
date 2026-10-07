class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans  = 0
        
        for i in range(n):
            freq = [0] * 26
            for j in range( i , n):
                #as we move j we increment the frequency arr
                freq[ord(s[j]) - ord('a')] += 1
                maxFreq = 0
                minFreq = float('inf')

                for freqCount in freq :
                    if freqCount > 0:
                        maxFreq = max(maxFreq , freqCount)
                        minFreq = min(minFreq, freqCount)

                ans += maxFreq - minFreq
                
        return ans

        