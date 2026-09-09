class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # atp len(s) == len(t)
        # sort both strings, chars sorted in alphabetical order
        new_s = sorted(s)
        new_t = sorted(t)
        # check if both indices are the same value,
        for c_s, c_t in zip(new_s, new_t):
            # if not --> not an anagram
            if c_s != c_t:
                return False

        return True



        