class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        # Total number of elements that should be on the left side
        left_partition_size = (m + n + 1) // 2

        while left <= right:

            # How many elements do we take from each array
            partition1 = (left + right) // 2
            partition2 = left_partition_size - partition1

            # Elements immediately around partition1
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]

            # Elements immediately around partition2
            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition:
            # everything on the left <= everything on the right
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # nums1 contributes too many elements to the left
            elif left1 > right2:
                right = partition1 - 1

            # nums1 contributes too few elements to the left
            else:
                left = partition1 + 1