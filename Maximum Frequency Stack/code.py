class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x, self.tail)
            self.tail.next = node
            self.tail = node

    def pop(self) -> int:
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        return val

    def peek(self) -> int:
        return self.tail.val

    def empty(self) -> bool:
        return self.head is None

class FreqStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> int:
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()