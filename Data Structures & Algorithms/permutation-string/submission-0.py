class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # populate s1 dict
        s1_dict = {}

        for c in s1:
            if(c not in s1_dict):
                s1_dict[c] = 1
            else:
                s1_dict[c] += 1
        
        # check if s1 permutation in s2
        for i, c in enumerate(s2):
            win_size_max = i + len(s1) - 1
            if(win_size_max < len(s2)):
                s2_dict = {}
                # get the substring from i to i + len(s1) - 1
                tmp_i = i
                while tmp_i <= win_size_max:
                    # populate s2_dict
                    c = s2[tmp_i]
                    if(c not in s2_dict):
                        s2_dict[c] = 1
                    else:
                        s2_dict[c] += 1
                    tmp_i += 1
                
                # check if the 2 dicts are equal
                if(s2_dict == s1_dict):
                    return True
        

        return False

