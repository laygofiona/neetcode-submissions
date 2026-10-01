class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        idx = 0
        stack = []
        if len(tokens) == 1:
            return int(tokens[-1])

        while idx < len(tokens):
            if tokens[idx] not in ('+', '-', '*', '/'):
                # its a number so add to stack
                stack.append(tokens[idx])
            else:
                # its an operator
                sec_operand = int(stack[-1])
                stack.pop()
                fir_operand = int(stack[-1])
                stack.pop()

                res = None

                if tokens[idx] == '+':
                    res = fir_operand + sec_operand
                elif tokens[idx] == '-':
                    res = fir_operand - sec_operand
                elif tokens[idx] == '*':
                    res = fir_operand * sec_operand
                else:
                    res = int(fir_operand / sec_operand)
                
                stack.append(res)
            idx += 1
        
        return stack[-1]
