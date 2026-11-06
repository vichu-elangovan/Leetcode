"""
387. First Unique Character in a String  (Easy)
https://leetcode.com/problems/first-unique-character-in-a-string/

Approach
--------
Two passes with a dictionary.
1. Count how many times each character appears in the string.
2. Walk the string again in order and return the index of the first
   character whose count is exactly 1. If no character qualifies,
   return -1.

The second pass must go over the string (not the dictionary) so that
"first" respects the original order of characters.

Time:  O(n) - two linear passes, O(1) average dictionary operations
Space: O(1) - the dictionary holds at most 26 lowercase letters
"""


class Solution:
    def firstUniqChar(self, s):
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx

        return -1


# --- Solved example --------------------------------------------------------
# Input: s = "loveleetcode"
#
# Pass 1 (count):
#   {'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}
#
# Pass 2 (find first with count 1):
#   idx=0 'l' -> count 2, skip
#   idx=1 'o' -> count 2, skip
#   idx=2 'v' -> count 1  -> return 2
#
# Output: 2

if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))        # 0
    print(s.firstUniqChar("loveleetcode"))    # 2
    print(s.firstUniqChar("aabb"))            # -1
