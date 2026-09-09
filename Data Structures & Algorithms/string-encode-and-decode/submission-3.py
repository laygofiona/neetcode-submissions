import re
class Solution:

    def encode(self, strs: List[str]) -> str:

        sizes = []
        res = ""

        # go through each element in list
        # and get the size of the lement
        for word in strs:
            sizes.append(len(word))
        
        # go through each element in strs
        i = 0
        while i < len(strs):
            # append the size of the current string
            res += str(sizes[i])
            # append the delimeter #
            res += "#"
            # append the actual word
            res += str(strs[i])
            i = i + 1
        
        return res


    def decode(self, s: str) -> List[str]:
        # create an array res
        res = []


        # go through each character in the string
        i = 0
        while(i < len(s)):
            j = i
            # find the size of the word or number
            # go through each char until # is reached
            # and number hasn't been read
            while(s[j] != "#"):
                j += 1
            
            # reached the # symbol so j is now at the #
            # need to get characters from i to j - 1
            # that will be our size
            size = int(s[i:j])

            # the next size characters from j will be our word
            # so extract that and append that to res
            word = s[j + 1:size + j + 1]
            res.append(word)
            # make sure i points to the next number/size
            i = j + size + 1
        return res
        
        

