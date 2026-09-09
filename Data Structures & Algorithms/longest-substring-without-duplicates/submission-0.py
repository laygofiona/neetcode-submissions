class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        res = 0

        l = 0

        for r in range(len(s)):
            # check if r is in the set
            # if it is in the set, then remove it from the set
            # and increment l
            while(s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            
            # otherwise, it isn't in the set
            # add to the set
            charSet.add(s[r])
            

            # find the current max substring length
            res = max(r - l + 1, res)
            # R - L + 1

        return res