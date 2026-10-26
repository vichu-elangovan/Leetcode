"""
24. Swap Nodes in Pairs  (Medium)
https://leetcode.com/problems/swap-nodes-in-pairs/

Approach
--------
Swap the nodes themselves (not just their values) two at a time. A dummy
node placed before head means the first pair doesn't need special
handling. `prev` always points to the node just before the current pair.
For each pair (a, b):
1. a.next = b.next   -> a skips over b and points to the rest of the list
2. b.next = a        -> b now points back to a
3. prev.next = b     -> the previous part of the list links to b
4. prev = a          -> a is now the tail of the swapped pair, so it
                        becomes the new "node before the next pair"

The loop stops when fewer than two nodes remain.

Time:  O(n) - each node is visited once
Space: O(1) - only a few pointers, nodes are relinked in place
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:

            a = prev.next
            b = a.next
            a.next = b.next
            b.next = a
            prev.next = b
            prev = a

        return dummy.next


# --- Solved example --------------------------------------------------------
# Input: head = 1 -> 2 -> 3 -> 4 -> None
#
# dummy -> 1 -> 2 -> 3 -> 4,  prev = dummy
#
# Pair (1, 2):  a=1, b=2
#   a.next = b.next  -> 1 -> 3
#   b.next = a       -> 2 -> 1
#   prev.next = b    -> dummy -> 2
#   prev = a (1)
#   list now: dummy -> 2 -> 1 -> 3 -> 4
#
# Pair (3, 4):  a=3, b=4
#   a.next = b.next  -> 3 -> None
#   b.next = a       -> 4 -> 3
#   prev.next = b    -> 1 -> 4
#   prev = a (3)
#   list now: dummy -> 2 -> 1 -> 4 -> 3
#
# prev.next is None -> loop ends, return dummy.next
#
# Output: 2 -> 1 -> 4 -> 3 -> None

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
    print(to_list(s.swapPairs(build([1, 2, 3, 4]))))   # [2, 1, 4, 3]
    print(to_list(s.swapPairs(build([1, 2, 3]))))      # [2, 1, 3]
    print(to_list(s.swapPairs(build([]))))             # []
    print(to_list(s.swapPairs(build([1]))))            # [1]
