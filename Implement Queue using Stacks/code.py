class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x: int) -> None:
        if self.top is None:
            self.top = Node(x)
        else:
            node = Node(x, self.top)
            self.top.next = node
            self.top = node

    def pop(self) -> int:
        val = self.top.val
        self.top = self.top.prev
        return val

    def peek(self) -> int:
        return self.top.val

    def empty(self) -> bool:
        return self.top is None

class MyQueue:

    # def __init__(self):
    #     self.stack = Node()

    # def push(self, x: int) -> None:
    #     if self.stack.val is None:
    #         self.stack.val = x
    #     else:
    #         node = self.stack
    #         while node.next is not None:
    #             node = node.next
    #         node.next = Node(x, node)

    # def pop(self) -> int:
    #     val = self.stack.val
    #     self.stack = self.stack.next
    #     if self.stack is not None:
    #         self.stack.prev = None
    #     return val

    # def peek(self) -> int:
    #     return self.stack.val

    # def empty(self) -> bool:
    #     return self.stack is None

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    
    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
# param_3 = obj.peek()
param_4 = obj.empty()