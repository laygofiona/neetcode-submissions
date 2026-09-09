class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if(s[l] != s[r]):
                return False
            else:
                l += 1
                r -= 1
        
        return True
    def validPalindrome(self, s: str) -> bool:
        # loop through each character in s
        # extract new string from beginning to end, excluding the current character
        # call isPalindrome on that string
        # if it returns false, then we return false
        for idx in range(len(s)):
            # extract new string (first half) from beginning to idx
            first_half = s[:idx]
            # from idx + 1 to the end of s
            second_half = s[idx + 1:]

            
            string = first_half + second_half
            print(string)
            if(Solution.isPalindrome(string) == True):
                return True

        # otherwise, reached the end, no valid palindrome
        return False
        