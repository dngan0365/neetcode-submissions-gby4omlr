class Node:
    def __init__(self, val=-1, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.dummyHead = Node(-1)
        self.dummyTail = Node(-1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def isEmpty(self) -> bool:
        if self.dummyHead.next == self.dummyTail:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.dummyTail
        new_node.prev = self.dummyTail.prev

        self.dummyTail.prev.next = new_node
        self.dummyTail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.prev = self.dummyHead
        new_node.next = self.dummyHead.next

        self.dummyHead.next.prev = new_node
        self.dummyHead.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        pop_node = self.dummyTail.prev
        value = pop_node.val

        self.dummyTail.prev = pop_node.prev
        pop_node.prev.next = self.dummyTail

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        pop_node = self.dummyHead.next
        value = pop_node.val

        pop_node.next.prev = self.dummyHead
        self.dummyHead.next = pop_node.next

        return value
