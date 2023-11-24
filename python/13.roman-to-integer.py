#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        Romandict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += Romandict[char]
        return number
           

        

#10,1,1
#Solution().romanToInt("XII")
#1,5
#print(Solution().romanToInt("IV"))
# @lc code=end

"""
# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}
 
# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
 
# print key with val 100
position = val_list.index(100)
print(key_list[position])
"""
