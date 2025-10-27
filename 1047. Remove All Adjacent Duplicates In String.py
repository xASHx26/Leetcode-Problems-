class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if not stack or i !=stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)

'''
just using simple stack 
'''

