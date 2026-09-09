class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            # turn array into a set to avoid duplicates
            nums_set = set(nums)

            # find the start of any possible sequence
            # loop through the array nums
            i = 0
            max_len = 1
            while i < len(nums):
                # a number is the start of a sequence if it doesn't have a left neighbor
                # a left neighbor is a consecutive number before it (num - 1)
                # check if there isn't a left neighbor
                if(nums[i] - 1 not in nums_set):
                    # then current num[i] is the start of a sequence
                    # check if there is the following number after that, num + 1
                    curr_len = 1
                    next_num = nums[i] + 1
                    while(next_num in nums_set):
                        # found the next number
                        # increment curr_len
                        curr_len += 1
                        next_num += 1
                    # update max_len
                    max_len = max(curr_len, max_len)
                i += 1
            
            return max_len
                    




