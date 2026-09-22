"""
1929. Concatenation of Array  (Easy)
https://leetcode.com/problems/concatenation-of-array/

Approach
--------
Build a copy of nums, then use list multiplication (2 * arr) to
duplicate the whole list and append it to itself in one step.

Time:  O(n) - building the copy and duplicating are both linear
Space: O(n) - the output array, size 2n
"""


class Solution(object):
    def getConcatenation(self, nums):
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i])
        arr = 2 * arr
        return arr


# --- Solved example --------------------------------------------------------
# Input: nums = [1, 2, 1]
#
# arr = [1, 2, 1]           (copy built from the loop)
# arr = 2 * [1, 2, 1]
#     = [1, 2, 1, 1, 2, 1]  (list repeated twice)
#
# Output: [1, 2, 1, 1, 2, 1]

if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([1, 2, 1]))      # [1, 2, 1, 1, 2, 1]
    print(s.getConcatenation([1, 3, 2, 1]))   # [1, 3, 2, 1, 1, 3, 2, 1]
