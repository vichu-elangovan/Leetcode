"""
707. Design Linked List  (Medium)
https://leetcode.com/problems/design-linked-list/

Approach
--------
Implement a singly linked list from scratch with a Node class holding
val/next, and a MyLinkedList class exposing get, addAtHead, addAtTail,
addAtIndex, and deleteAtIndex.

- get(index): walk from head, counting nodes, return val at index or
  -1 if out of range.
- addAtHead: create a node, point it at the current head, make it the
  new head.
- addAtTail: create a node, walk to the last node, attach it there
  (special-cased if the list is currently empty).
- addAtIndex: walk to the node just *before* index (current < index-1),
  then splice the new node in. index == 0 is delegated to addAtHead.
- deleteAtIndex: same walk-to-before-the-node approach, then relink
  around the target node to remove it. index == 0 is handled directly
  by moving head forward.

Time:  O(k) per operation, where k is the index being accessed
       (O(n) worst case for tail operations)
Space: O(n) - total nodes stored across the list
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):

        temp = self.head
        current = 0

        while temp:

            if current == index:
                return temp.val

            temp = temp.next
            current += 1

        return -1

    def addAtHead(self, val):

        newNode = Node(val)

        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode

    def addAtIndex(self, index, val):

        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head
        current = 0

        while temp and current < index - 1:
            temp = temp.next
            current += 1

        if temp is None:
            return

        newNode = Node(val)

        newNode.next = temp.next
        temp.next = newNode

    def deleteAtIndex(self, index):

        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        current = 0

        while temp.next and current < index - 1:
            temp = temp.next
            current += 1

        if temp.next:
            temp.next = temp.next.next


# --- Solved example --------------------------------------------------------
# Operations:
#   addAtHead(1)         -> list: 1
#   addAtTail(3)         -> list: 1,3
#   addAtIndex(1, 2)     -> list: 1,2,3   (insert 2 at index 1)
#   get(1)               -> 2
#   deleteAtIndex(0)     -> list: 2,3     (removes head)
#   get(0)               -> 2
#
# Output: [None, None, None, 2, None, 2]

if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)     # list: 1->2->3
    print(obj.get(1))        # 2
    obj.deleteAtIndex(0)     # list: 2->3
    print(obj.get(0))        # 2
