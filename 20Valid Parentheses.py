class Solution(object):
    def isValid(self, s):
        stack=[]
        mapp={"(":")","{":"}" ,"[":"]"}
        for i in s:
            if i in mapp:
                stack.append(i)

            elif i in mapp.values():
                if not stack or mapp[stack[-1]]!=i:
                    return False
                stack.pop()
            else:
                return False

        return len(stack)==0

# create a stack then use create a hasmap for opening paranthesis as key and closing as value
#loop over array if you find any opening paranthesis append them over to the stack
#if map values match with closing parantasis pop top 


#return true if stack is empty








            



            

        