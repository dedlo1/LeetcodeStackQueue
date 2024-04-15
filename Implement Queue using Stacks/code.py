class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyQueue:

    def __init__(self):
        self.stack = Node()

    def push(self, x: int) -> None:
        if self.stack.val is None:
            self.stack.val = x
        else:
            node = self.stack
            while node.next is not None:
                node = node.next
            node.next = Node(x, node)

    def pop(self) -> int:
        val = self.stack.val
        self.stack = self.stack.next
        if self.stack is not None:
            self.stack.prev = None
        return val

    def peek(self) -> int:
        return self.stack.val

    def empty(self) -> bool:
        return self.stack.val is None and self.stack.next is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()