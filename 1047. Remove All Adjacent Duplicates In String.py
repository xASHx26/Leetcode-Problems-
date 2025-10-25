class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if s[i] not in stack:
                stack.append(i)
            else:
                stack.pop()
        return stack



        