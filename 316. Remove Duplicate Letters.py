class Solution(object):
    def removeDuplicateLetters(self, s):
        # Initialize an empty stack to build the result
        # 'minsort' keeps track of the last index of each letter in 's'
        # 'seen' is a set to record which letters have already been added to the stack
        stack = []
        minsort = {letter: i for i, letter in enumerate(s)}
        seen = set()

        # Iterate through each letter in the string
        for i, letter in enumerate(s):
            # Only process letters that have not been added before
            if letter not in seen:
                # If the current letter is smaller than the last letter in the stack
                # and the last letter will appear again later,
                # pop it from the stack to maintain lexicographical order
                while stack and letter < stack[-1] and i < minsort[stack[-1]]:
                    seen.discard(stack.pop())

                # Add the current letter to the stack and mark it as seen
                seen.add(letter)
                stack.append(letter)

        # Join the stack into a string and return the final result
        return "".join(stack)


'''
📝 NOTE:
For finding the lexicographically smallest result with no duplicate letters:
1. Create a stack to build the final sequence.
2. Use a dictionary (minsort) to track the last occurrence index of each character.
3. Use a set (seen) to remember which characters are already in the stack.
4. While traversing, pop larger letters that appear again later to maintain order.
5. The final stack gives the smallest possible string with all unique letters.
'''
