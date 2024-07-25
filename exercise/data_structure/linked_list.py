class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: ListNode | None = None


# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


# 插入
def insert(n0, p):
    """在n0后插入节点p"""
    p = ListNode(6)
    p.next = n1
    n0.next = p


# 删除
def remove(n0):
    """删除n0后的节点p"""
    if not n0.next:
        return
    p = n0.next
    n1 = p.next
    n0.next = n1


# 访问
def access(head: ListNode, index: int) -> ListNode | None:
    if not head:
        return None
    for _ in range(index):
        head = head.next
    return head


# print(access(n0, 2).val)

# 查找
def find(head: ListNode, val: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    index = 0
    while head:
        if head.val == val:
            return index
        else:
            index += 1
            head = head.next
    return -1


print(find(n0, 4))
