class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]


'''
if left is gratter then right
L     M     R
4,5,6,7,0,1,2
and nums[mid]>nums[right]
then left =mid+1

      M l   R
4,5,6,7,0,1,2
    

        l M R
4,5,6,7,0,1,2

          R
        l M 
4,5,6,7,0,1,2

'''

