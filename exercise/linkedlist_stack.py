class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: ListNode | None = None


class LinkedListStack:
    """基于链表实现的栈"""

    def __init__(self):
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, val: int):
        p = ListNode(val)
        p.next = self._peek
        self._peek = p
        self._size += 1

    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val

    def pop(self):
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def to_list(self):
        node = self._peek
        arr = []
        while node:
            arr.append(node)
            node = node.next
        return arr
