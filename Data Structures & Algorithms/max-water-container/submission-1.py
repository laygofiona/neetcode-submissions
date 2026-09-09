class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area of water = min(h1, h2) * 2

        # create a max_area variable to keep track of current max_area
        max_area = float("-inf")

        # loop through each height in heights
        # for each height, loop through its following heights
        h1_idx = 0
        while(h1_idx < len(heights) -1):
            h2_idx = h1_idx + 1
            while(h2_idx < len(heights)):
                # check if current height * following height area is greater than max_area
                #set max_area to that area if greater
                length = min(heights[h1_idx], heights[h2_idx]) 
                width = h2_idx - h1_idx
                area = length * width
                max_area = max(area, max_area)
                h2_idx += 1
            h1_idx += 1
        

        # return max_area
        return max_area
        