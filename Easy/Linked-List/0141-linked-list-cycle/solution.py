"""
141. Linked List Cycle  (Easy)
https://leetcode.com/problems/linked-list-cycle/

Approach
--------
Floyd's cycle detection (tortoise and hare). Two pointers start at
head: slow moves one step at a time, fast moves two. If there's no
cycle, fast reaches the end (None) and the loop exits normally. If
there IS a cycle, fast will eventually "lap" slow and they'll land on
the same node, confirming a cycle.

Time:  O(n) - fast pointer catches slow within one full lap of the cycle
Space: O(1) - only two pointers, no extra memory
"""


class Solution(object):
    def hasCycle(self, head):

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False


# --- Solved example --------------------------------------------------------
# Input: head = 3 -> 2 -> 0 -> 4 -> (back to node 2, cycle)
#
# slow=3, fast=3
#
# step1: slow=2, fast=0         -> not equal
# step2: slow=0, fast=2         -> not equal
# step3: slow=4, fast=4         -> equal! -> return True
#
# Output: True

if __name__ == "__main__":
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    s = Solution()

    # build a cycle manually: 3 -> 2 -> 0 -> 4 -> back to 2
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle back to node 2
    print(s.hasCycle(n1))   # True

    # no cycle
    a = ListNode(1)
    a.next = ListNode(2)
    print(s.hasCycle(a))    # False
