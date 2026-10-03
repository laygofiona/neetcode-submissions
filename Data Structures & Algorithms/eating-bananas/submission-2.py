import math
class Solution:

    def test(self, k, piles, h):
        curr_h = 0
        for pile in piles:
            res = math.ceil(pile / k)
            curr_h += res

            if curr_h > h:
                return False
        if curr_h > h:
            return False
        else: 
            return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while l <= r:
            k = (l + r) // 2
            if self.test(k, piles, h):
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        
       
        
