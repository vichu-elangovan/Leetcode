"""
1512. Number of Good Pairs  (Easy)
https://leetcode.com/problems/number-of-good-pairs/

Approach
--------
Brute force: check every pair (i, j) with j > i and count how many
pairs have equal values.

Time:  O(n^2) - nested loop over all pairs
Space: O(1)   - just a counter
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count = count + 1

        return count


# --- Solved example --------------------------------------------------------
# Input: nums = [1, 2, 3, 1, 1, 3]
#
# i=0(1) j=1(2): 1!=2         no
# i=0(1) j=2(3): 1!=3         no
# i=0(1) j=3(1): 1==1  count=1
# i=0(1) j=4(1): 1==1  count=2
# i=0(1) j=5(3): 1!=3         no
# i=1(2) j=2..5: no matches
# i=2(3) j=3(1): no
# i=2(3) j=4(1): no
# i=2(3) j=5(3): 3==3  count=3
# i=3(1) j=4(1): 1==1  count=4
# i=3(1) j=5(3): no
# i=4(1) j=5(3): no
#
# Output: 4

if __name__ == "__main__":
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 4
    print(s.numIdenticalPairs([1, 1, 1, 1]))        # 6
    print(s.numIdenticalPairs([1, 2, 3]))           # 0
