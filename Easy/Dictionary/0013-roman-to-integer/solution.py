"""
13. Roman to Integer  (Easy)
https://leetcode.com/problems/roman-to-integer/

Approach
--------
Map each roman numeral to its value with a hash table. Walk the string
left to right: normally we add a symbol's value, but if a symbol is
smaller than the one right after it (e.g. 'I' before 'V' in "IV"), it's
a subtractive pair, so we subtract it instead. The final character is
always added on its own since it has no symbol after it to compare to.

Time:  O(n) - single pass over the string
Space: O(1) - the values map has a fixed size (7 symbols)
"""


class Solution:
    def romanToInt(self, s):
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0

        for i in range(len(s)-1):
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total + values[s[-1]]


# --- Solved example --------------------------------------------------------
# Input: s = "MCMXCIV"
#
# i=0 'M'(1000) vs 'C'(100)  -> 1000 not < 100  -> total += 1000 -> 1000
# i=1 'C'(100)  vs 'M'(1000) -> 100 < 1000      -> total -= 100  -> 900
# i=2 'M'(1000) vs 'X'(10)   -> not <            -> total += 1000 -> 1900
# i=3 'X'(10)   vs 'C'(100)  -> 10 < 100         -> total -= 10   -> 1890
# i=4 'C'(100)  vs 'I'(1)    -> not <            -> total += 100  -> 1990
# i=5 'I'(1)    vs 'V'(5)    -> 1 < 5            -> total -= 1    -> 1989
# last char 'V' added on its own -> 1989 + 5 = 1994
#
# Output: 1994

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))       # 3
    print(s.romanToInt("LVIII"))     # 58
    print(s.romanToInt("MCMXCIV"))   # 1994
