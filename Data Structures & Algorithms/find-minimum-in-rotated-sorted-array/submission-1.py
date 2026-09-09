class Solution:
    def findMin(self, nums: List[int]) -> int:
        # make a L, R pointer
        L, R = 0, len(nums) - 1

        # In the end, our left pointer will point to the minimum element
        while L < R:
            mid = (R + L) // 2
            # if mid is greater than the right pointer
            # then the second half is unsorted
            # otherwise if mid is less than the right pointer
            # then the second half is sorted, we want to move right to mid, to go to the unsorted portion
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid + 1
        
        return nums[L]
            



        