"""
817. Linked List Components  (Medium)
https://leetcode.com/problems/linked-list-components/

Approach
--------
A "component" is a maximal run of consecutive nodes whose values are all
in nums. Instead of tracking runs explicitly, count where each run ENDS:
a node ends a component if its value is in nums and the next node is
either missing (end of list) or not in nums. Each component has exactly
one such end node, so counting them gives the answer.

Putting nums into a set makes each membership check O(1) on average.

Time:  O(n + m) - n = list length, m = len(nums) to build the set
Space: O(m)     - the set of nums
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def numComponents(self, head, nums):

        s = set(nums)

        count = 0

        curr = head

        while curr:

            if curr.val in s and (curr.next is None or curr.next.val not in s):
                count += 1

            curr = curr.next
        return count


# --- Solved example --------------------------------------------------------
# Input: head = 0 -> 1 -> 2 -> 3 -> 4, nums = [0, 3, 1, 4]
#
# s = {0, 1, 3, 4}
#
# curr=0: in s, next=1 in s        -> not an end, count=0
# curr=1: in s, next=2 not in s    -> end of component [0,1], count=1
# curr=2: not in s                 -> skip
# curr=3: in s, next=4 in s        -> not an end, count=1
# curr=4: in s, next is None       -> end of component [3,4], count=2
#
# Output: 2   (components: [0,1] and [3,4])

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
    print(s.numComponents(build([0, 1, 2, 3]), [0, 1, 3]))      # 2
    print(s.numComponents(build([0, 1, 2, 3, 4]), [0, 3, 1, 4]))  # 2
