from __future__ import annotations
# 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
from dataclasses import dataclass
from typing import Optional
# Definition for singly-linked list.
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
    def __init__(self, val_list):
        if val_list:
            self.head = ListNode(val_list[0])
        else:
            self.head = None
        last_node = self.head
        for val in val_list[1:]:
            node = ListNode(val)
            last_node.next = node
            last_node = node

    def getHead(self):
        return self.head

    def __repr__(self):
        node = self.head
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return str(result)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        jin = 0
        first_flag = 0 # 作用是确定第一次算出的val要赋给head,以后就新建一个node，并串上last one
        head = ListNode()
        last_node = head
        while l1 or l2 or jin:  # 如果还有进位也要继续算，直到进位也没了
            bit_sum = jin
            if l1:
                bit_sum += l1.val
                l1 = l1.next
            if l2:
                bit_sum += l2.val
                l2 = l2.next
            jin = bit_sum // 10
            node_val = bit_sum % 10
            if first_flag == 0:
                head.val = node_val
            else:
                cur_node = ListNode(val=node_val)
                last_node.next = cur_node
                last_node = cur_node
            first_flag = 1
        return head
if __name__ == '__main__':
    solution = Solution()
    l1 = LinkList([9])
    l2 = LinkList([0])
    # print(l1)
    print(solution.addTwoNumbers(l1.head, l2.head))