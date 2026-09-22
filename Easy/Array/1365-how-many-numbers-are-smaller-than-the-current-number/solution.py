"""
1365. How Many Numbers Are Smaller Than the Current Number  (Easy)
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Approach
--------
Brute force: for every number in nums, scan the entire array and count
how many other elements (excluding itself, by index) are smaller than it.

Time:  O(n^2) - nested loop, n elements each scanning all n elements
Space: O(n)   - the output array (not counting the output, O(1) extra)
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []

        for i in range(len(nums)):

            count = 0

            for j in range(len(nums)):

                if i != j and nums[j] < nums[i]:

                    count += 1

            arr.append(count)

        return arr


# --- Solved example --------------------------------------------------------
# Input: nums = [8, 1, 2, 2, 3]
#
# i=0 (val=8): compare against 1,2,2,3 -> all smaller -> count=4
# i=1 (val=1): compare against 8,2,2,3 -> none smaller -> count=0
# i=2 (val=2): compare against 8,1,2,3 -> only 1 smaller -> count=1
# i=3 (val=2): compare against 8,1,2,3 -> only 1 smaller -> count=1
# i=4 (val=3): compare against 8,1,2,2 -> 1,2,2 smaller -> count=3
#
# Output: [4, 0, 1, 1, 3]

if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [4, 0, 1, 1, 3]
    print(s.smallerNumbersThanCurrent([6, 5, 4, 8]))     # [2, 1, 0, 3]
    print(s.smallerNumbersThanCurrent([7, 7, 7, 7]))     # [0, 0, 0, 0]
