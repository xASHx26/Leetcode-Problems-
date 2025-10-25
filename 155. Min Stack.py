class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.MinStack=[]

    def push(self, val):
        self.stack.append(val)
        val=min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)

    def pop(self):
        self.stack.pop()
        self.MinStack.pop()
        

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



'''
solution:
for getting the problem solven in o(1)
i used onther stack to get the min of that stack 
'''