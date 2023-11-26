#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = (sorted(set(nums)))
        print(nums)
        
        dups = []
        for i in nums:
            if i not in dups:
                dups.append(i)

        print(nums)
        #return (dups)
        

Solution().removeDuplicates([1,1,2])
# @lc code=end

