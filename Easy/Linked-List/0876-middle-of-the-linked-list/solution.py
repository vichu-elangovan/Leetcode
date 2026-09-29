"""
876. Middle of the Linked List  (Easy)
https://leetcode.com/problems/middle-of-the-linked-list/

Approach
--------
Fast and slow pointers (tortoise and hare). Both start at head. Each
step, `slow` moves one node while `fast` moves two. By the time `fast`
reaches the end of the list, `slow` has covered exactly half the
distance, landing it on the middle node (or the second of the two
middle nodes, for an even-length list).

Time:  O(n) - single pass, fast pointer visits each node at most once
Space: O(1) - only two pointers
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 2 -> 3 -> 4 -> 5 -> None
#
# slow=1, fast=1
#
# step1: fast(1) and fast.next(2) exist -> slow=2, fast=3
# step2: fast(3) and fast.next(4) exist -> slow=3, fast=5
# step3: fast(5) exists but fast.next is None -> loop stops
#
# return slow -> node with val 3
#
# Output: 3 -> 4 -> 5 -> None

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
    print(to_list(s.middleNode(build([1, 2, 3, 4, 5]))))       # [3, 4, 5]
    print(to_list(s.middleNode(build([1, 2, 3, 4, 5, 6]))))    # [4, 5, 6]
