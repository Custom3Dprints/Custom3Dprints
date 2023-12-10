#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        lis = []
        for i in nums:
            if i != val:
                lis.append(i)

        
        return len(lis)

#print(Solution().removeElement([3,2,2,3], 3))
#Solution().removeElement([0,1,2,2,3,0,4,2], 2)
        
# @lc code=end

