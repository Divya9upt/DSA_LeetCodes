class MyQueue:
    def __init__(self):
        self.to_push = []
        self.to_pop = []
        

    def push(self, x: int) -> None:
        self.to_push.append(x)


    def _fillPop(self) -> None:
        if not self.to_pop:
            while self.to_push:
                self.to_pop.append(self.to_push.pop())


    def pop(self) -> int:
        self._fillPop()
        return self.to_pop.pop()
        

    def peek(self) -> int:
        self._fillPop()
        return self.to_pop[-1]
        

    def empty(self) -> bool:
        return not self.to_push and not self.to_pop
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()