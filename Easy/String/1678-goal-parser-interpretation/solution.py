"""
1678. Goal Parser Interpretation  (Easy)
https://leetcode.com/problems/goal-parser-interpretation/

Approach
--------
The command string is made of three tokens: "G", "()" and "(al)".
"G" already stays "G", so only the other two need rewriting:
- "()"   becomes "o"
- "(al)" becomes "al"
Two chained str.replace() calls handle both. Order doesn't matter here
because the two patterns never overlap.

Time:  O(n) - each replace scans the string once
Space: O(n) - new strings are created
"""


class Solution(object):
    def interpret(self, command):
        return command.replace('()', 'o').replace('(al)', 'al')


# --- Solved example --------------------------------------------------------
# Input: command = "G()(al)"
#
# replace '()'   with 'o'  -> "Go(al)"
# replace '(al)' with 'al' -> "Goal"
#
# Output: "Goal"
#
# Input: command = "G()()()()(al)"
#
# replace '()'   with 'o'  -> "Goooo(al)"
# replace '(al)' with 'al' -> "Goooooal"   (four 'o's, then "al")
#
# Output: "Gooooal"

if __name__ == "__main__":
    s = Solution()
    print(s.interpret("G()(al)"))          # Goal
    print(s.interpret("G()()()()(al)"))    # Gooooal
    print(s.interpret("(al)G(al)()()G"))   # alGalooG
