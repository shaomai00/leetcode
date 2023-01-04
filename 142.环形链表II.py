# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 构建两次相遇，第一次相遇时fast回退到head指针
        # 然后一起一步一步走，直到第二次相遇时slow和fast都共同指向的是入环节点。因为slow从相遇节点出发 经历a+nb步，fast从头结点出发 经历a步
        fast,slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while True:
            if fast == slow: return fast
            fast, slow = fast.next, slow.next
