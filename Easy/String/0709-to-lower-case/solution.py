"""
709. To Lower Case  (Easy)
https://leetcode.com/problems/to-lower-case/

Approach
--------
Python's built-in str.lower() returns a copy of the string with every
uppercase letter converted to lowercase. Characters that are already
lowercase, or aren't letters at all, are left unchanged.

Time:  O(n) - each character is visited once
Space: O(n) - a new string is created
"""


class Solution(object):
    def toLowerCase(self, s):
        return s.lower()


# --- Solved example --------------------------------------------------------
# Input: s = "Hello"
#
# 'H' -> 'h'
# 'e' -> 'e'  (already lowercase)
# 'l' -> 'l'
# 'l' -> 'l'
# 'o' -> 'o'
#
# Output: "hello"
#
# Input: s = "LOVELY"
#
# Output: "lovely"

if __name__ == "__main__":
    s = Solution()
    print(s.toLowerCase("Hello"))     # hello
    print(s.toLowerCase("here"))      # here
    print(s.toLowerCase("LOVELY"))    # lovely
