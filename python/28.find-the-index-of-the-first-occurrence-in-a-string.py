#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution(object):
  def strStr(self, haystack, needle):
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                return i
    return -1

   
print(Solution().strStr("mississippi", "issip"))
#Solution().strStr("sadbutad", "ad")
# @lc code=end

"""
if needle == '':
    return 0
for i in range(len(haystack)-len(needle)+1):
    for j in range(len(needle)):
        if haystack[i+j] != needle[j]:
            break
        if j == len(needle)-1:
            return i
return -1

def strStr(self, haystack, needle):
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                return i
    return -1
"""