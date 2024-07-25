class ArrayStack:
    """基于数组实现的栈"""

    def __init__(self):
        self._stack = []

    def size(self):
        return len(self._stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]

    def to_list(self):
        return self._stack
