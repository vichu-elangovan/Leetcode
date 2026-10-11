"""
2130. Maximum Twin Sum of a Linked List  (Medium)
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

Approach
--------
In a list of even length n, node i and node (n-1-i) are "twins". To pair
them without extra memory:
1. Find the middle with slow/fast pointers (slow ends at the start of
   the second half).
2. Reverse the second half in place, so its first node is the original
   tail, which is the twin of the head.
3. Walk both halves together (head forward, reversed half forward),
   adding each twin pair and keeping the maximum sum.

Time:  O(n) - find middle, reverse, and compare are each linear
Space: O(1) - reversal is in place, no extra list or array
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def pairSum(self, head):

        slow = head
        fast = head

        # find middle

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head
        right = prev
        ans = 0
        while right:

            ans = max(ans, left.val + right.val)

            left = left.next
            right = right.next

        return ans


# --- Solved example --------------------------------------------------------
# Input: head = 5 -> 4 -> 2 -> 1 -> None   (n = 4)
#
# Find middle:
#   slow=5, fast=5
#   step1: slow=4, fast=2
#   step2: slow=2, fast=None -> stop. slow is at index 2 (val 2)
#
# Reverse second half (2 -> 1) becomes (1 -> 2), prev points to node 1
#
# Compare twins:
#   left=5, right=1 -> sum 6, ans=6
#   left=4, right=2 -> sum 6, ans=6
#   right is None -> loop ends
#
# Output: 6

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
    print(s.pairSum(build([5, 4, 2, 1])))       # 6
    print(s.pairSum(build([4, 2, 2, 3])))       # 7
    print(s.pairSum(build([1, 100000])))        # 100001
