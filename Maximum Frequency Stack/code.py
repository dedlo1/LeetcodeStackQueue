from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None




class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stack = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 1
        else:
            self.freq[val] += 1
        if self.freq[val] not in self.stack:
            self.stack[self.freq[val]] = deque()
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.stack[self.freq[val]].append(node)

    def pop(self) -> int:
        max_freq = max(self.stack.keys())
        node = self.stack[max_freq].pop()
        if len(self.stack[max_freq]) == 0:
            del self.stack[max_freq]
        self.freq[node.val] -= 1
        if self.freq[node.val] == 0:
            del self.freq[node.val]
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()