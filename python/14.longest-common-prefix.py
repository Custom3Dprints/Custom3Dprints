#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        Strs = list(zip(*strs))
        common = ''
        for i in Strs:
            if "".join(list(i)) == list(i)[0]*len(list(i)):
                common += list(i)[0]
            else:
                return common
        return common
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            print(i, l)
            print(set(i))
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

Solution().longestCommonPrefix(["flower","flow","flight"])
# @lc code=end