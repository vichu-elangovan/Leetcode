"""
202. Happy Number  (Easy)
https://leetcode.com/problems/happy-number/

Approach
--------
Repeatedly replacing n with the sum of the squares of its digits
either eventually reaches 1 (happy) or falls into an infinite cycle
that never reaches 1 (not happy). This is exactly the "does this
sequence loop" problem, so we reuse Floyd's cycle detection
(slow/fast pointers) — but here each "step" is calling nxt() instead
of following a .next pointer.

slow advances one nxt() call per iteration, fast advances two. If a
cycle exists, slow and fast will eventually land on the same value.
Once they meet, that shared value is 1 only if the number is happy.

Time:  O(log n) per nxt() call (number of digits), cycle detection
       adds a small constant factor on top
Space: O(1) - no extra structures, just a couple of integers
"""


class Solution(object):
    def isHappy(self, n):

        def nxt(num):

            s = 0

            while num:

                rem = num % 10
                s = s + rem * rem
                num = num // 10

            return s

        slow = n
        fast = nxt(n)

        while slow != fast:

            slow = nxt(slow)

            fast = nxt(nxt(fast))

        return slow == 1


# --- Solved example --------------------------------------------------------
# Input: n = 19
#
# nxt(19) = 1^2+9^2 = 1+81 = 82
# nxt(82) = 64+4 = 68
# nxt(68) = 36+64 = 100
# nxt(100) = 1+0+0 = 1
# nxt(1) = 1   (stays at 1 forever once reached)
#
# slow=19, fast=nxt(19)=82
#
# slow!=fast -> slow=nxt(19)=82,  fast=nxt(nxt(82))=nxt(68)=100
# slow!=fast -> slow=nxt(82)=68,  fast=nxt(nxt(100))=nxt(1)=1
# slow!=fast -> slow=nxt(68)=100, fast=nxt(nxt(1))=nxt(1)=1
# slow!=fast -> slow=nxt(100)=1,  fast=nxt(nxt(1))=1
# slow==fast (both 1) -> loop ends
#
# return slow == 1 -> True
#
# Output: True

if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))   # True
    print(s.isHappy(2))    # False
