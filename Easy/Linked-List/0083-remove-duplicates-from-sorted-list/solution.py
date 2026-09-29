"""
83. Remove Duplicates from Sorted List  (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Approach
--------
Since the list is sorted, duplicates are always adjacent. Walk through
with a single pointer `temp`: if the current node's value equals the
next node's value, skip over the next node by relinking temp.next.
Otherwise, advance temp normally. No new "previous" pointer is needed
since duplicates are removed by looking one node ahead.

Time:  O(n) - single pass through the list
Space: O(1) - no new nodes, just pointer rewiring
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):

        temp = head
        while temp and temp.next:

            if temp.val == temp.next.val:
                temp.next = temp.next.next

            else:
                temp = temp.next

        return head


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 1 -> 2 -> 3 -> 3 -> None
#
# temp=1
# temp.val(1) == temp.next.val(1) -> temp.next = 2  -> list: 1->2->3->3
# temp.val(1) != temp.next.val(2) -> temp=2
# temp.val(2) != temp.next.val(3) -> temp=3
# temp.val(3) == temp.next.val(3) -> temp.next = None -> list: 1->2->3
# temp.next is None -> loop ends
#
# Output: 1 -> 2 -> 3 -> None

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
    print(to_list(s.deleteDuplicates(build([1, 1, 2]))))          # [1, 2]
    print(to_list(s.deleteDuplicates(build([1, 1, 2, 3, 3]))))    # [1, 2, 3]
