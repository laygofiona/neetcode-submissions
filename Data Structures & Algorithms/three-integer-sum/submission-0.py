class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_arr = nums

        # sort nums first
        nums_arr.sort()
        # create array to store output results
        results = []
        # have num loop through nums
        # create pointers i and j where i is one pos after num and j is at the end of the list
        # in each loop of nums, loop from i to j
        
        for num_idx, num in enumerate(nums_arr):
            # skip duplicates for num
            if(num_idx > 0 and nums[num_idx] == nums[num_idx - 1]):
                continue
            # i points to the element after num
            i = num_idx + 1
            # j points to the last element in nums
            j = len(nums_arr) - 1
            # loop through each element between i and j
            # check their sum with num
            while i < j:
                curr_sum = num + nums_arr[i] + nums_arr[j]
                # check if their sum(i + j + num) is equal to 0
                if(curr_sum == 0):
                    # append it to results array 
                    results.append([num, nums_arr[i], nums_arr[j]])

                    # skip duplicates for i
                    while(i < j and nums[i + 1] == nums[i]):
                        i += 1
                    # skip duplicates for j
                    while(i < j and nums[j - 1] == nums[j]):
                        j -= 1
                    
                    i += 1
                    j -= 1
                    
                elif(curr_sum < 0):
                    # move i up 1 position
                    i += 1
                elif(curr_sum > 0):
                    # sum is greater than 0
                    # move j down 1 position 
                    j -= 1
                

        return results