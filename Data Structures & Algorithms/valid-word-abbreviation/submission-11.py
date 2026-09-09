class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # define two pointers
        # ptr i for word
        i = 0
        # ptr j for abbr
        j = 0
        # go through all the chars in word and abbr
        while i < len(word) and j < len(abbr):
            # check if the characters are the same
            if(word[i] == abbr[j]):
                # move on to the next character
                i += 1
                j += 1
            elif(abbr[j].isdigit()):
                # it is a number
                if(int(abbr[j]) == 0):
                    return False
                # extract the number
                start = j
                while(j < len(abbr) and abbr[j].isdigit()):
                    j += 1
                # increment i by that number
                i += int(abbr[start:j])
            else:
                return False
                   
        
        if(i == len(word) and j == len(abbr)):
            return True
        else:
            return False
        





