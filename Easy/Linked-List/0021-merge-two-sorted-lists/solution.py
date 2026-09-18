"""
21. Merge Two Sorted Lists  (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

Approach
--------
Use a dummy head node so we don't have to special-case the first
insertion. Walk both lists at the same time with two pointers, always
attaching the smaller of the two current nodes to the result and
advancing that list's pointer. Once one list runs out, attach whatever
remains of the other list in one go (it's already sorted).

Time:  O(n + m) - n, m are the lengths of list1 and list2
Space: O(1)      - reuses existing nodes, no new nodes created
                   (the dummy node is the only extra allocation)

Note: requires a ListNode class:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        res = ListNode(0)
        cur = res

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return res.next


# --- Solved example --------------------------------------------------------
# Input: list1 = [1,2,4], list2 = [1,3,4]
#
# res = dummy(0), cur = dummy
#
# 1 <= 1  -> attach list1(1), cur -> 1, list1 -> [2,4]
# 3 <= 2? no (2<=3) -> attach list1(2), cur -> 2, list1 -> [4]
# 4 <= 3? no (3<=4) -> attach list2(3), cur -> 3, list2 -> [4]
# 4 <= 4  -> attach list1(4), cur -> 4, list1 -> []
# list1 is empty -> loop ends
# cur.next = list2 (remaining [4])
#
# Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4
#
# Output: [1,1,2,3,4,4]

if __name__ == "__main__":
    class ListNode:
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
    l1 = build([1, 2, 4])
    l2 = build([1, 3, 4])
    print(to_list(s.mergeTwoLists(l1, l2)))   # [1, 1, 2, 3, 4, 4]
