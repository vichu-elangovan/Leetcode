"""
203. Remove Linked List Elements  (Easy)
https://leetcode.com/problems/remove-linked-list-elements/

Approach
--------
First, strip off any matching values right at the head (possibly
several in a row), since removing the head means reassigning `head`
itself. Once head is either None or a non-matching value, walk the
rest of the list with `temp`: whenever the *next* node matches val,
skip over it by relinking temp.next; otherwise just advance normally.
(Checking one node ahead is what lets us delete without needing a
separate "previous" pointer.)

Time:  O(n) - single pass through the list
Space: O(1) - no new nodes, just pointer rewiring
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeElements(self, head, val):

        while head and head.val == val:
            head = head.next

        temp = head

        while temp and temp.next:

            if temp.next.val == val:
                temp.next = temp.next.next

            else:
                temp = temp.next

        return head


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None, val = 6
#
# head.val=1 != 6 -> skip the head-stripping loop, head stays at 1
#
# temp=1
# temp.next=2, 2!=6           -> temp=2
# temp.next=6, 6==6           -> temp.next = 6.next (3)  -> list: 1->2->3->4->5->6
# temp.next=3, 3!=6           -> temp=3
# temp.next=4, 4!=6           -> temp=4
# temp.next=5, 5!=6           -> temp=5
# temp.next=6, 6==6           -> temp.next = 6.next (None) -> list: 1->2->3->4->5
# temp.next is None -> loop ends
#
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

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

    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    s = Solution()
    print(to_list(s.removeElements(build([1, 2, 6, 3, 4, 5, 6]), 6)))  # [1, 2, 3, 4, 5]
    print(to_list(s.removeElements(build([7, 7, 7, 7]), 7)))           # []
