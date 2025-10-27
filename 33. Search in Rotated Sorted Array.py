class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1

        # Step 1: Find rotation point (smallest element)
        while left < right:
            mid = (left + right) // 2

            '''
            if nums[mid] > nums[right]:
            L     M     R
            4, 5, 6, 7, 0, 1, 2
            then left = mid + 1

                  M l   R
            4, 5, 6, 7, 0, 1, 2

                        l M R
            4, 5, 6, 7, 0, 1, 2

                              R
                            l M
            4, 5, 6, 7, 0, 1, 2

            else:
            nums[mid] <= nums[right]
            right = mid
            '''
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        min_index = left  # smallest element index

        # Step 2: Decide which side to search
        if min_index == 0:
            # Array not rotated
            left, right = 0, n - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            # Target in left part
            left, right = 0, min_index - 1
        else:
            # Target in right part
            left, right = min_index, n - 1

        # Step 3: Normal binary search
        while left <= right:
            mid = (left + right) // 2

            '''
            Binary search steps:
            L   M   R
            0   3   6
            check nums[mid] == target
            if target > nums[mid] -> left = mid + 1
            if target < nums[mid] -> right = mid - 1
            '''
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
