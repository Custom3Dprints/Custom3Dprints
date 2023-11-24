#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        numToIndex = {}
        for i in range(len(nums)):
            print(target - nums[i], numToIndex)
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """



# @lc code=end

