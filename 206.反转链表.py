from __future__ import annotations
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
from typing import Optional
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int = 0
    next: ListNode = None
    def __repr__(self):
        result = [self.val]
        node = self.next
        while node:
            result.append(node.val)
            node = node.next
        return str(result)

class LinkList:
    def __init__(self, list):
        self.head = ListNode(list[0]) if list else None
        last_node = self.head
        for num in list[1:]:
            node = ListNode(num)
            last_node.next = node
            last_node = node
    def __repr__(self):
        return str(self.head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list_head = None
        cur_node = head
        while cur_node:
            # 原始链表中的下一位先存好
            node = cur_node.next
            # 把当前链表的下一位返过来
            cur_node.next = reversed_list_head
            # 新链表头后移
            reversed_list_head = cur_node
            # 原始链表后移
            cur_node = node
        return reversed_list_head
# c node
# 9->5->1->4->none
# None<-9 5->1->4

if __name__ == '__main__':
    solution = Solution()
    l1 = LinkList([9,5,1])
    # l2 = LinkList([0])
    print(solution.reverseList(l1.head))