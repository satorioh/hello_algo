class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: ListNode | None = None


class LinkedListQueue:
    """基于链表实现的队列"""

    def __init__(self):
        self._front = None  # 头节点
        self._rear = None  # 尾节点
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0

    def push(self, num):
        node = ListNode(num)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
            self._size += 1

    def peek(self):
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val

    def pop(self):
        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num

    def to_list(self):
        arr = []
        node = self._front
        while node:
            arr.append(node.val)
            node = node.next
        return arr
