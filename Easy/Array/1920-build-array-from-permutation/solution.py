"""
1920. Build Array from Permutation  (Easy)
https://leetcode.com/problems/build-array-from-permutation/

Approach
--------
For each index i, the answer is nums[nums[i]] — a direct double
lookup into the original array using its own values as indices.

Time:  O(n) - single pass building the result
Space: O(n) - the output array
"""


class Solution(object):
    def buildArray(self, nums):

        arr = []

        for i in range(len(nums)):

            arr.append(nums[nums[i]])

        return arr


# --- Solved example --------------------------------------------------------
# Input: nums = [0, 2, 1, 5, 3, 4]
#
# i=0: nums[nums[0]] = nums[0] = 0
# i=1: nums[nums[1]] = nums[2] = 1
# i=2: nums[nums[2]] = nums[1] = 2
# i=3: nums[nums[3]] = nums[5] = 4
# i=4: nums[nums[4]] = nums[3] = 5
# i=5: nums[nums[5]] = nums[4] = 3
#
# Output: [0, 1, 2, 4, 5, 3]

if __name__ == "__main__":
    s = Solution()
    print(s.buildArray([0, 2, 1, 5, 3, 4]))  # [0, 1, 2, 4, 5, 3]
    print(s.buildArray([5, 0, 1, 2, 3, 4]))  # [4, 5, 0, 1, 2, 3]
