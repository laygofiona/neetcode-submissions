class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            # sort the array in ascending order
            nums.sort()

            # remove duplicates
            arr = []

            for i, num in enumerate(nums):
                if(nums[i] not in arr):
                    arr.append(nums[i])
            
            L, R = 0, 1

            max_len = 1

            while R < len(arr):
                if(arr[R] - arr[R - 1] != 1):
                    L = R
                max_len = max(R - L + 1, max_len)
                R += 1
            return max_len


