"""
287. Find the Duplicate Number  (Medium)
https://leetcode.com/problems/find-the-duplicate-number/

Approach
--------
nums contains n+1 integers in the range [1, n], so by pigeonhole at
least one value repeats. Treat each index/value pair as a pointer:
from index i, "nums[i]" tells you which index to jump to next. Because
there's a duplicate value, two different indices eventually point into
the same chain, creating a cycle — exactly like a linked list cycle.

Phase 1: slow/fast pointers (1x/2x speed, via nums[slow] / nums[nums[fast]])
find a meeting point inside the cycle, same as Floyd's algorithm.

Phase 2: reset slow to nums[0] (the start), then move slow and fast one
step at a time together. Where they meet is the cycle's entry point —
which is guaranteed to be the duplicate number itself.

Time:  O(n) - linear in both phases
Space: O(1) - no extra structures; this is the whole point of this
              approach vs. a hash-set which would use O(n) space
"""


class Solution(object):
    def findDuplicate(self, nums):

        slow = nums[0]
        fast = nums[0]

        while True:

            slow = nums[slow]

            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# --- Solved example --------------------------------------------------------
# Input: nums = [1,3,4,2,2]
#
# Phase 1 (find meeting point):
#   slow=nums[0]=1, fast=nums[0]=1
#   slow=nums[1]=3, fast=nums[nums[1]]=nums[3]=2
#   slow=nums[3]=2, fast=nums[nums[2]]=nums[4]=2
#   slow==fast (both 2) -> break
#
# Phase 2 (find entry point):
#   slow=nums[0]=1, fast stays at 2
#   slow!=fast -> slow=nums[1]=3, fast=nums[2]=4
#   slow!=fast -> slow=nums[3]=2, fast=nums[4]=2
#   slow==fast (both 2) -> loop ends
#
# Output: 2

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))     # 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))     # 3
