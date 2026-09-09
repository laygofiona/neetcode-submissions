from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each word
        # create a frequency letter arr for each word
        # convert that to a tuple
        # check if it exists in the dictionary, add word to values
        # return dictionary values
        my_dict = defaultdict()
        for word in strs:
            freq_arr = [0] * 26
            for char in word:
                pos = ord(char) - ord('a')
                freq_arr[pos] += 1
            key = tuple(freq_arr)
            if tuple(freq_arr) not in my_dict:
                my_dict[key] = [word]
            else:
                my_dict[key].append(word)
        
        res = []
        for val in my_dict.values():
            res.append(val)
        return res
                    



        

        