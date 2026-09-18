"""
14. Longest Common Prefix  (Easy)
https://leetcode.com/problems/longest-common-prefix/

Approach
--------
Use the first string as a reference. Walk through its characters one
index at a time, and at each index check that every other string has
the same character at that position. The moment a mismatch is found
(or a word runs out of characters), the prefix up to that point is the
answer. If we make it through the entire first string without a
mismatch, the whole first string is the common prefix.

Time:  O(S) - S is the sum of all characters in all strings (worst case)
Space: O(1) - no extra structures, just slicing the result
"""


class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        for i in range(len(strs[0])):

            for word in strs[1:]:

                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]


# --- Solved example --------------------------------------------------------
# Input: strs = ["flower", "flow", "flight"]
#
# strs[0] = "flower"
#
# i=0 'f': flow[0]='f' ok, flight[0]='f' ok
# i=1 'l': flow[1]='l' ok, flight[1]='l' ok
# i=2 'o': flow[2]='o' ok, flight[2]='i' != 'o'  -> mismatch!
#          return strs[0][:2] -> "fl"
#
# Output: "fl"

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
    print(s.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # "inters"
