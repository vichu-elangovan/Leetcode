"""
142. Linked List Cycle II (medium)
https://leetcode.com/problems/linked-list-cycle-ii/

Approach
--------
Floyd's cycle detection, extended to find the cycle's starting node.

Phase 1: slow/fast pointers move at 1x/2x speed as usual. If they
meet, a cycle exists.

Phase 2: once slow and fast meet, reset a new pointer `temp` to head.
Move `temp` and `slow` one step at a time together. The point where
they meet is mathematically guaranteed to be the start of the cycle
(this follows from the distance relationships between head, the
cycle start, and the meeting point in phase 1).

If fast ever reaches the end (None), there's no cycle, so return None.

Time:  O(n) - linear in both phases
Space: O(1) - only a few pointers
"""


class Solution(object):
    def detectCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next

                return temp
        return None


# --- Solved example --------------------------------------------------------
# Input: head = 3 -> 2 -> 0 -> 4 -> (back to node 2, cycle starts at node 2)
#
# Phase 1 (find meeting point):
#   slow=3, fast=3
#   step1: slow=2, fast=0
#   step2: slow=0, fast=2
#   step3: slow=4, fast=4  -> meet! fast == slow (both at node 4)
#
# Phase 2 (find cycle start):
#   temp=head(3), slow=4(from phase 1)
#   temp(3) != slow(4) -> temp=2, slow=2
#   temp(2) == slow(2) -> loop ends, return temp
#
# Output: node with val 2 (the cycle's starting node)

if __name__ == "__main__":
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    s = Solution()

    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle starts at node 2
    result = s.detectCycle(n1)
    print(result.val if result else None)   # 2

    a = ListNode(1)
    a.next = ListNode(2)
    print(s.detectCycle(a))   # None
