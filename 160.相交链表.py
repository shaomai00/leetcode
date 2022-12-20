# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null
# 两个指针依次遍历两个链表的每个节点,
# 每步操作需要同时更新指针pA 和pB。
# 如果指针pA 不为空，则将指针pA 移到下一个节点；如果指针pB 不为空，则将指针pB 移到下一个节点。
# 如果指针pA 为空，则将指针pA 移到链表headB 的头节点；如果指针pB 为空，则将指针pB 移到链表headA 的头节点。
# 当指针pA 和 pB 指向同一个节点或者都为空时，返回它们指向的节点或者null
from typing import Optional
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        if not headA or not headB:
            return None
        for _ in range(2):
            while pa and pb:
                pa = pa.next
                pb = pb.next
            if not pa:
                pa = headB
            if not pb:
                pb = headA
        while pa != pb and pa and pb:
            pa = pa.next
            pb = pb.next
        if pa == pb:
            return pb
        else:
            return None


