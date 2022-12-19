# 给你一个链表的头节点 head ，判断链表中是否有环。
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        quick_pointer = head
        slow_pointer = head
        first = True
        while quick_pointer and quick_pointer.next:
            if not first and quick_pointer == slow_pointer:
                return True
            first = False
            quick_pointer = quick_pointer.next.next
            slow_pointer = slow_pointer.next
        return False