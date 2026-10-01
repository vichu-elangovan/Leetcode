"""
26. Remove Duplicates from Sorted Array  (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach
--------
Two pointers. Since the array is sorted, all duplicates are adjacent.
`k` tracks the position where the next unique value should go (starts
at 1, since nums[0] is always unique by definition). Walk through with
"i"; whenever nums[i] differs from the previous element (nums[i-1]),
it's a new unique value — write it at position k and advance k.

The array is modified in place; k is returned as the count of unique
elements (the first k slots of nums hold them, order preserved).

Time:  O(n) - single pass
Space: O(1) - done in place, no extra array
"""


class Solution(object):
    def removeDuplicates(self, nums):

        k = 1  # first element is not duplicate

        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]:

                nums[k] = nums[i]

                k += 1

        return k


# --- Solved example --------------------------------------------------------
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
#
# k=1
# i=1: nums[1]=0 == nums[0]=0        -> skip
# i=2: nums[2]=1 != nums[1]=0        -> nums[1]=1, k=2
# i=3: nums[3]=1 == nums[2]=1        -> skip
# i=4: nums[4]=1 == nums[3]=1        -> skip
# i=5: nums[5]=2 != nums[4]=1        -> nums[2]=2, k=3
# i=6: nums[6]=2 == nums[5]=2        -> skip
# i=7: nums[7]=3 != nums[6]=2        -> nums[3]=3, k=4
# i=8: nums[8]=3 == nums[7]=3        -> skip
# i=9: nums[9]=4 != nums[8]=3        -> nums[4]=4, k=5
#
# nums is now [0,1,2,3,4,...] (first 5 slots), k=5
#
# Output: 5, with nums = [0,1,2,3,4,_,_,_,_,_]

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 1, 2]
    print(s.removeDuplicates(nums1), nums1[:2])              # 2 [1, 2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums2), nums2[:5])              # 5 [0, 1, 2, 3, 4]
