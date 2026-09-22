"""
1480. Running Sum of 1d Array  (Easy)
https://leetcode.com/problems/running-sum-of-1d-array/

Approach
--------
Keep a running total as we walk through the array once, appending the
total-so-far after adding each element.

Time:  O(n) - single pass
Space: O(n) - the output array
"""


class Solution(object):
    def runningSum(self, nums):
        arr = []
        s = 0

        for i in range(len(nums)):
            s = s + nums[i]

            arr.append(s)

        return arr


# --- Solved example --------------------------------------------------------
# Input: nums = [1, 2, 3, 4]
#
# i=0: s = 0+1 = 1   -> arr = [1]
# i=1: s = 1+2 = 3   -> arr = [1, 3]
# i=2: s = 3+3 = 6   -> arr = [1, 3, 6]
# i=3: s = 6+4 = 10  -> arr = [1, 3, 6, 10]
#
# Output: [1, 3, 6, 10]

if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1, 2, 3, 4]))       # [1, 3, 6, 10]
    print(s.runningSum([1, 1, 1, 1, 1]))    # [1, 2, 3, 4, 5]
    print(s.runningSum([3, 1, 2, 10, 1]))   # [3, 4, 6, 16, 17]
