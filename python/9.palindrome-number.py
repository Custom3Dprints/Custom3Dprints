#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        if(str(x) == str(x)[::-1]):
            return True
        return False
        """
        :type x: int
        :rtype: bool
        """
# @lc code=end

