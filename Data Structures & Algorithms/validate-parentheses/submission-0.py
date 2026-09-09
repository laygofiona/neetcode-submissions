class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # read through each char in string
        for char in s:
            # if the char is an opening bracket we want to push it to a stack
            if(char == '(' or char == '[' or char == '{'):
                stack.append(char)
            else:
                # char is a closing bracket we want to pop out the item in the stack and check if it is the same 
                if(len(stack) > 0):
                    opening_bracket = stack.pop()
                    if((opening_bracket == '(' and char != ')') or (opening_bracket == '[' and char != ']') or (opening_bracket == '{' and char != '}')):
                        return False
                else:
                    return False
                    # otherwise return false


        # return true at the end
        if(len(stack) > 0):
            return False

        return True
        