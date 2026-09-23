"""
217. Contains Duplicate  (Easy)
https://leetcode.com/problems/contains-duplicate/

Approach
--------
Walk through nums while keeping a set of values seen so far. If a value
is already in the set, a duplicate has been found. Otherwise add it and
keep going. If the loop finishes without a match, all values are unique.

A one-line alternative using set() directly:
    return len(nums) != len(set(nums))
(converting to a set drops duplicates, so a length mismatch means at
least one duplicate existed)

Time:  O(n) - single pass, O(1) average set lookups/inserts
Space: O(n) - the set can hold up to n elements
"""


class Solution(object):
    def containsDuplicate(self, nums):

        visit = set()

        for i in range(len(nums)):

            if nums[i] in visit:

                return True

            visit.add(nums[i])

        return False


or

class Solution(object):
    def containsDuplicate(self, nums):

          return len(nums) != len(set(nums))


# --- Solved example --------------------------------------------------------
# Input: nums = [1, 2, 3, 1]
#
# i=0: 1 not in {}        -> visit = {1}
# i=1: 2 not in {1}       -> visit = {1, 2}
# i=2: 3 not in {1, 2}    -> visit = {1, 2, 3}
# i=3: 1 IS in {1, 2, 3}  -> return True
#
# Output: True

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))        # True
    print(s.containsDuplicate([1, 2, 3, 4]))        # False
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
