"""
1290. Convert Binary Number in a Linked List to Integer  (Easy)
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Approach
--------
Each node holds a single bit (0 or 1), most significant bit first.
Walk the list once, building the number the way you'd build any binary
value left to right: at each step, shift the accumulated value left by
one bit (ans * 2) and add in the current bit.

Time:  O(n) - single pass through the list
Space: O(1) - just an accumulator
"""


class Solution:
    def getDecimalValue(self, head):
        ans = 0

        while head:

            ans = ans * 2 + head.val

            head = head.next

        return ans


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 0 -> 1 -> None   (binary "101")
#
# ans=0
# head.val=1: ans = 0*2 + 1 = 1
# head.val=0: ans = 1*2 + 0 = 2
# head.val=1: ans = 2*2 + 1 = 5
#
# Output: 5   (binary 101 = decimal 5)

if __name__ == "__main__":
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build(lst):
        dummy = ListNode(0)
        cur = dummy
        for v in lst:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    s = Solution()
    print(s.getDecimalValue(build([1, 0, 1])))        # 5
    print(s.getDecimalValue(build([0])))               # 0
    print(s.getDecimalValue(build([1, 1, 0, 0, 1])))   # 25
