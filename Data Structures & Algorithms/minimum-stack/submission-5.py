class MinStack:
    stack = None
    stack_len = None
    min_arr = None

    def __init__(self):
        self.stack = []
        self.stack_len = -1
        self.min_arr = []

    def push(self, val: int) -> None:
        if len(self.min_arr) == 0:
            self.min_arr.append(val)
        else:
            if self.min_arr[len(self.min_arr) - 1] >= val:
                self.min_arr.append(val)
        self.stack_len += 1
        self.stack.append(val)
        return None
        

    def pop(self) -> None:
        # update current_min to remove
        if self.stack[self.stack_len] == self.min_arr[len(self.min_arr) - 1]:
            # self.current_min = self.prev_min
            del self.min_arr[-1]
        self.stack.pop()
        self.stack_len -= 1
        return None
        

    def top(self) -> int:
        return self.stack[self.stack_len]
        

    def getMin(self) -> int:
        return self.min_arr[len(self.min_arr) - 1]
        
