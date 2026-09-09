class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # point to the beginning
        L, R = 0, 0

        # store the counts of characters in the current window
        curr_win = {}

        # to keep track of ouptut
        longest = float("-inf")

        # move our R pointer all the way until it reaches the end of s
        for R in range(0, len(s)):
            # update our curr_win
            # if the character exists, then we increment
            if s[R] in curr_win:
                curr_win[s[R]] += 1
            # otherwise, create a new entry at 1
            else:
                curr_win[s[R]] = 1
            

            # find the most common element (key) in the window
            common_elem = max(curr_win, key=curr_win.get)

            # Get the most common element value
            common_elem_val = curr_win[common_elem]

            # Get the number of non-common elements
            res = (R - L + 1) - common_elem_val

            # check if res is more than k
            if res > k:
                # create a new window
                # update the counter value of the current L in dict 
                curr_win[s[L]] -= 1
                # move L up by 1 position
                L += 1
            
            # update the current longest value
            longest = max(longest, R - L + 1)
        
        if longest == float("-inf"):
            return 0
        else:
            return longest


