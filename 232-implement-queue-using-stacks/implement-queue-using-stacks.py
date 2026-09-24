class MyQueue:

    class MyStack:

            def __init__(self):
                self.Capacity = 100
                self.Top = -1
                self.arr = [None] * self.Capacity

            def push(self, x: int) -> None:        
                
                self.Top += 1

                

                self.arr[self.Top] = x

            def pop(self) -> int:
                if(self.empty()): return None

                data = self.arr[self.Top]

                self.Top = self.Top - 1

                return data
                

            def peek(self) -> int:
                return self.arr[self.Top]

            def empty(self) -> bool:
                return self.Top == -1

            def Resize(self) ->None:
                self.arr.extend([None] * self.Capacity)
                self.Capacity *= 2


    def __init__(self):
        self.Stack1 = self.MyStack()
        self.Stack2 = self.MyStack()
         

    def push(self, x: int) -> None:
        while(not self.Stack2.empty()):
            self.Stack1.push(self.Stack2.pop())

        self.Stack1.push(x)

        while(not self.Stack1.empty()):
            self.Stack2.push(self.Stack1.pop())

        
    def pop(self) -> int:
        return self.Stack2.pop()
        

    def peek(self) -> int:
        return self.Stack2.peek()

    def empty(self) -> bool:
        return self.Stack2.empty()
        

    

# Your MyQueue object will be instantiated and called as such:
#obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()