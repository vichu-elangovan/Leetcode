"""
457. Circular Array Loop  (Medium)
https://leetcode.com/problems/circular-array-loop/

Approach
--------
Treat the array as a graph: from index i, the next index is
(i + nums[i]) % n, so the array wraps around circularly. A valid loop
must (a) be a cycle, (b) have length > 1, and (c) move in one
direction only (all positive or all negative values).

For every starting index, run Floyd's slow/fast pointers:
- slow moves 1 step, fast moves 2 steps.
- If any visited value has a different sign from the start
  (direction), this path can't be a valid loop, so stop.
- If slow meets fast, a cycle exists. If slow points back to itself
  (a self-loop of length 1), it's invalid; otherwise return True.

If no starting index produces a valid cycle, return False.

Time:  O(n^2) worst case - each of the n starts can walk up to O(n)
       steps. (Marking dead-end indices as visited, e.g. setting them
       to 0, brings this down to O(n).)
Space: O(1) - only a few pointers
"""


class Solution(object):
    def circularArrayLoop(self, nums):

        n = len(nums)

        def nextIndex(i):
            return (i + nums[i]) % n

        for i in range(n):

            direction = nums[i] > 0

            slow = i
            fast = i

            while True:

                # slow moves 1 step
                next_slow = nextIndex(slow)

                if (nums[next_slow] > 0) != direction:
                    break

                # fast moves 1st step
                next_fast = nextIndex(fast)

                if (nums[next_fast] > 0) != direction:
                    break

                # fast moves 2nd step
                next_fast = nextIndex(next_fast)

                if (nums[next_fast] > 0) != direction:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:

                    # self loop (length 1) is invalid
                    if slow == nextIndex(slow):
                        break

                    return True

        return False


# --- Solved example --------------------------------------------------------
# Input: nums = [2, -1, 1, 2, 2]      (n = 5)
#
# Start i=0, direction = positive
#   slow=0, fast=0
#
#   round 1: next_slow = (0+2)%5 = 2   (nums[2]=1  > 0 ok)
#            next_fast = 2             (ok)
#            next_fast = (2+1)%5 = 3   (nums[3]=2  > 0 ok)
#            slow=2, fast=3            -> not equal
#
#   round 2: next_slow = (2+1)%5 = 3   (ok)
#            next_fast = (3+2)%5 = 0   (nums[0]=2  > 0 ok)
#            next_fast = (0+2)%5 = 2   (ok)
#            slow=3, fast=2            -> not equal
#
#   round 3: next_slow = (3+2)%5 = 0   (ok)
#            next_fast = (2+1)%5 = 3   (ok)
#            next_fast = (3+2)%5 = 0   (ok)
#            slow=0, fast=0            -> equal!
#            slow != nextIndex(0)=2, so not a self-loop -> return True
#
# The loop is 0 -> 2 -> 3 -> 0, all positive moves.
#
# Output: True

if __name__ == "__main__":
    s = Solution()
    print(s.circularArrayLoop([2, -1, 1, 2, 2]))          # True
    print(s.circularArrayLoop([-1, -2, -3, -4, -5, 6]))   # False
    print(s.circularArrayLoop([-2, 1, -1, -2, -2]))       # False
