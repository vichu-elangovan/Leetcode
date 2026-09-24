"""
1. Two Sum  (Easy)
https://leetcode.com/problems/two-sum/

Approach
--------
Brute force: check every pair (i, j) with j > i and return the indices
as soon as their values add up to the target.

Time:  O(n^2) - nested loop over all pairs
Space: O(1)   - no extra data structures used
"""


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]




# --- Solved example --------------------------------------------------------
# Input:  nums = [2, 7, 11, 15], target = 9
#
# i=0, j=1  nums[0]+nums[1] = 2+7  = 9  == target  -> return [0, 1]
#
# Output: [0, 1]   because nums[0] + nums[1] == 2 + 7 == 9

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # [1, 2]
    print(s.twoSum([3, 3], 6))           # [0, 1]
