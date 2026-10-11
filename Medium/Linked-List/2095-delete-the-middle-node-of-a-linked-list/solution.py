"""
2095. Delete the Middle Node of a Linked List  (Medium)
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Approach
--------
Use slow/fast pointers to find the middle node: fast moves 2 steps while
slow moves 1, so when fast reaches the end, slow is on the middle node
(index n // 2). To delete it, we need the node just before it, so a
second walk from head runs until temp.next is slow, then relinks
temp.next to skip over it.

Edge case: a list with 0 or 1 nodes becomes empty after deleting the
middle, so we return None immediately.

Time:  O(n) - one pass to find the middle, one pass to find its predecessor
Space: O(1) - only a few pointers, no new nodes
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteMiddle(self, head):

        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = head

        while temp.next != slow:
            temp = temp.next

        temp.next = temp.next.next

        return head


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6 -> None   (n = 7)
#
# Find middle:
#   slow=1, fast=1
#   step1: slow=3, fast=4
#   step2: slow=4, fast=1 (second 1)
#   step3: slow=7, fast=6
#   fast.next is None -> stop. slow is the node with val 7 (index 3)
#
# Find predecessor:
#   temp=1 -> temp.next=3 != slow -> temp=3
#   temp=3 -> temp.next=4 != slow -> temp=4
#   temp=4 -> temp.next=7 == slow -> stop
#
# Delete: temp(4).next = temp.next.next = 1 (second 1)
#
# Output: 1 -> 3 -> 4 -> 1 -> 2 -> 6 -> None

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
    print(to_list(s.deleteMiddle(build([1, 3, 4, 7, 1, 2, 6]))))  # [1, 3, 4, 1, 2, 6]
    print(to_list(s.deleteMiddle(build([1, 2, 3, 4]))))           # [1, 2, 4]
    print(to_list(s.deleteMiddle(build([2, 1]))))                 # [2]
