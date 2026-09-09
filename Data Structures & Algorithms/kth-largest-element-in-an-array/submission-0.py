import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap
        # transform nums to a min heap
        heapq.heapify(nums)

        # pop len - k + 1 times to get to the largest elment
        times = len(nums) - k + 1

        num = None
        for i in range(times):
            num = heapq.heappop(nums)
        
        return num


        

        