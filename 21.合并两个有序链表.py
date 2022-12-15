# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
from typing import Optional
from dataclasses import dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

class LinkList:
    def __init__(self, nums):
        self.head = ListNode(nums[0])
        node = self.head
        for num in nums[1:]:
            cur_node = ListNode(val=num)
            node.next = cur_node
            node = node.next
    def __repr__(self):
        ll = []
        node = self.head
        while node:
            ll.append(node.val)
            node = node.next
        return str(ll)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = ListNode()
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                cur_node = ListNode(list1.val)
                list1 = list1.next
            else:
                cur_node = ListNode(list2.val)
                list2 = list2.next
            node.next = cur_node
            node = node.next
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return head.next

if __name__ == '__main__':
    l1 = LinkList([1, 2, 4])
    l2 = LinkList([1, 3, 4])
    sol = Solution()
    ll = sol.mergeTwoLists(l1.head,l2.head)
    while ll:
        print(ll)
        ll = ll.next
