class Solution(object):
    def repeatedCharacter(self, s):
        seen=set()
        for i in s:
            
            if i in seen:
                return i
            seen.add(i)
