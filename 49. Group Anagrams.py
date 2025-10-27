class Solution(object):
    def groupAnagrams(self, strs):
        result=defaultdict(list)

        for i in strs:
            count=[0]*26

            for c in i:
                count[ord(c)-ord("a")]+=1

            result[tuple(count)].append(i)
        return result.values()

'''

defaultdict automatcly assigns value to dic key

count has all the key of 0-26(a-z)

then we insert the ascki key of the charecters to  count

then we return values



'''
