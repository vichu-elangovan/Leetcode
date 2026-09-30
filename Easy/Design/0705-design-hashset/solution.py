"""
705. Design HashSet  (Easy)
https://leetcode.com/problems/design-hashset/

Approach
--------
Since key values are bounded (0 <= key <= 10^6 per the problem
constraints), we can use direct-address indexing: a fixed-size boolean
array where the key itself is the index. add/remove/contains all
become simple array writes/reads.

This trades memory for guaranteed O(1) operations — it doesn't scale
to arbitrary/unbounded keys, but is valid here since the key range is
known in advance.

Time:  O(1) - for add, remove, and contains
Space: O(N) - N = max possible key value, fixed array size regardless
              of how many keys are actually used
"""


class MyHashSet(object):

    def __init__(self):

        self.arr = [False] * 10000001

    def add(self, key):

        self.arr[key] = True

    def remove(self, key):

        self.arr[key] = False

    def contains(self, key):

        return self.arr[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# --- Solved example --------------------------------------------------------
# Operations: add(1), add(2), contains(1), contains(3), add(2), contains(2),
#             remove(2), contains(2)
#
# add(1)        -> arr[1] = True
# add(2)        -> arr[2] = True
# contains(1)   -> arr[1] = True   -> returns True
# contains(3)   -> arr[3] = False  -> returns False
# add(2)        -> arr[2] = True   (no-op, already True)
# contains(2)   -> arr[2] = True   -> returns True
# remove(2)     -> arr[2] = False
# contains(2)   -> arr[2] = False  -> returns False
#
# Output: [None, None, True, False, None, True, None, False]

if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))   # True
    print(obj.contains(3))   # False
    obj.add(2)
    print(obj.contains(2))   # True
    obj.remove(2)
    print(obj.contains(2))   # False
