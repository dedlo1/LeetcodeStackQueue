class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, x: int) -> None:
        if self.front is None:
            self.front = Node(x)
            self.back = self.front
        else:
            node = Node(x, self.back)
            self.back.next = node
            self.back = node

    def pop(self) -> int:
        val = self.front.val
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        return val

    def peek(self) -> int:
        return self.front.val

    def empty(self) -> bool:
        return self.front is None
    
    def __len__(self):
        length = 0
        node = self.front
        while node is not None:
            length += 1
            node = node.next
        return length



class MyStack:

    def __init__(self):
        self.queue = Queue()
        

    def push(self, x: int) -> None:
        self.queue.push(x)
        for _ in range(len(self.queue) - 1):
            self.queue.push(self.queue.pop())
        

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()