class Solution(object):
    def removeDuplicateLetters(self, s):
        stack=[]
        minsort={letter:i for i ,letter in enumerate(s)}
        seen=set()
        for i,letter in enumerate(s):
            if letter not in seen:
                while stack and letter<stack[-1] and i<minsort[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(letter)
                stack.append(letter)

        return "".join(stack)



'''

'''

        