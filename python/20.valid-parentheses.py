#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start

"""
true = ["()", "{}", "[]"]
class Solution(object):
    def isValid(self, s):

        s = "".join(sorted(s))
        print(s)
        if len(s) % 2 == 0:
            for i in range(len(s)):
                #print(i)
                if i % 2 == 0:
                    #print(s[i:i+2])
                    if s[i:i+2] not in true:
                        print (False)
                    else:
                        print (True)
        else:
            print (False)
"""
class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false


Solution().isValid("{()}") #true   work
Solution().isValid("([)]") #false  no work
# @lc code=end

