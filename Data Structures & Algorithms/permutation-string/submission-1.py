class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get length of s1 and create a window in s2
        L, R = 0, len(s1) - 1
        s1_cpy = ''.join(sorted(s1))

        while R < len(s2):
            s2_win_arr = s2[L : R + 1]
            s2_win_arr = sorted(s2_win_arr)
            # compare
            if ''.join(s2_win_arr) == s1_cpy:
                return True
            R += 1
            L += 1
        
        return False
            


