class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        
        def mergeSort(start, end):
            if start >= end :
                return 0

            mid = (start + end) //2
            count = mergeSort(start, mid) + mergeSort(mid + 1, end) #recursively break element before merge sort
            #counting the reverse pairs
            i = start 
            j = mid + 1
            while i <= mid and j <= end:
                if nums[i] > 2 * nums[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1
            
            temp = []
            #merge the sorted halves
            i = start 
            j = mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
                
            while i <= mid :
                temp.append(nums[i])
                i += 1
            while j <= end :
                temp.append(nums[j])
                j += 1

            nums[start:end + 1] = temp
            return count 

        return mergeSort(0, len(nums)-1)