"""
53. Maximum Subarray  (Medium)
https://leetcode.com/problems/maximum-subarray/

Approach
--------
Kadane's algorithm. Walk through the array once, keeping `cur_sum`, the
best sum of a subarray that ENDS at the current index. At each element
there are only two choices: extend the previous subarray (cur_sum + num)
or start fresh from this element (num). Take whichever is larger. If the
running sum has gone negative, starting fresh wins automatically.
`max_sum` records the best `cur_sum` seen at any index.

Time:  O(n) - single pass
Space: O(1) - two variables
"""


class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

            cur_sum = max(nums[i], cur_sum + nums[i])

            max_sum = max(cur_sum, max_sum)

        return max_sum


# --- Solved example --------------------------------------------------------
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# start: cur_sum = -2, max_sum = -2
#
# i=1 (1):  max(1, -2+1=-1)   = 1   -> cur_sum=1,  max_sum=1
# i=2 (-3): max(-3, 1-3=-2)   = -2  -> cur_sum=-2, max_sum=1
# i=3 (4):  max(4, -2+4=2)    = 4   -> cur_sum=4,  max_sum=4
# i=4 (-1): max(-1, 4-1=3)    = 3   -> cur_sum=3,  max_sum=4
# i=5 (2):  max(2, 3+2=5)     = 5   -> cur_sum=5,  max_sum=5
# i=6 (1):  max(1, 5+1=6)     = 6   -> cur_sum=6,  max_sum=6
# i=7 (-5): max(-5, 6-5=1)    = 1   -> cur_sum=1,  max_sum=6
# i=8 (4):  max(4, 1+4=5)     = 5   -> cur_sum=5,  max_sum=6
#
# Output: 6   (the subarray [4, -1, 2, 1])

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(s.maxSubArray([1]))                              # 1
    print(s.maxSubArray([5, 4, -1, 7, 8]))                 # 23
