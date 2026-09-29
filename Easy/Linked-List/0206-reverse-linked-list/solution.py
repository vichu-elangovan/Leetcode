"""
206. Reverse Linked List  (Easy)
https://leetcode.com/problems/reverse-linked-list/

Approach
--------
Iterative pointer reversal. Walk through the list once, and at each
node flip its `next` pointer to point backwards instead of forwards.
Three pointers are needed: `prev` (the reversed portion so far),
`curr` (the node being processed), and `nxt` (saved before we
overwrite curr.next, so we don't lose the rest of the list).

Time:  O(n) - single pass through the list
Space: O(1) - only a few pointers, no new nodes
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):

        prev = None

        curr = head

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 2 -> 3 -> None
#
# prev=None, curr=1
#
# step1: nxt=2, curr(1).next=None, prev=1, curr=2   -> reversed so far: 1->None
# step2: nxt=3, curr(2).next=1,    prev=2, curr=3   -> reversed so far: 2->1->None
# step3: nxt=None, curr(3).next=2, prev=3, curr=None -> reversed so far: 3->2->1->None
#
# loop ends (curr is None), return prev (node 3)
#
# Output: 3 -> 2 -> 1 -> None

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
    head = build([1, 2, 3, 4, 5])
    print(to_list(s.reverseList(head)))   # [5, 4, 3, 2, 1]
