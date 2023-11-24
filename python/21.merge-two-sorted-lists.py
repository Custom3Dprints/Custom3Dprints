#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        all = []
        for i in l1:
            all.append(i)
        for j in l2:
            all.append(j)

        #print(sorted(all))
        return sorted(all)


    
Solution().mergeTwoLists([],[0])
# @lc code=end

