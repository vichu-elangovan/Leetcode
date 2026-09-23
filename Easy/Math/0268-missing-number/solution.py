"""
268. Missing Number  (Easy)
https://leetcode.com/problems/missing-number/

Approach
--------
For n numbers that should contain every value from 0 to n (missing
exactly one), the sum of 0..n is a known formula: n*(n+1)/2. Subtract
the actual sum of the array from that expected sum — whatever's left
over is the missing number.

Time:  O(n) - one pass to sum the array
Space: O(1) - just two running totals
"""


class Solution(object):
    def missingNumber(self, nums):

        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum


# --- Solved example --------------------------------------------------------
# Input: nums = [3, 0, 1]
#
# n = 3
# expected_sum = 3*(3+1)//2 = 3*4//2 = 6   (sum of 0,1,2,3)
# actual_sum   = 3 + 0 + 1 = 4
#
# missing = 6 - 4 = 2
#
# Output: 2

if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))              # 2
    print(s.missingNumber([0, 1]))                 # 2
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))     # 8
