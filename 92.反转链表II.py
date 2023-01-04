# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
class LinkList:
    def __init__(self, list):
        self.head = ListNode(list[0]) if list else None
        last_node = self.head
        for num in list[1:]:
            node = ListNode(num)
            last_node.next = node
            last_node = node
    def __repr__(self):
        ll = []
        node = self.head
        while node:
            ll.append(node.val)
            node = node.next
        return str(ll)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 如果left=right就不用翻转了
        if not head or left == right:
            return head
        # 先找左端
        if left == 1:
            left_node = None
            reverse_head = head
        else:
            left_node = head
            for _ in range(left-2):
                left_node = left_node.next
            reverse_head = left_node.next
        # 再找右端
        right_node = reverse_head
        for _ in range(right-left):
            right_node = right_node.next
        reverse_tail = right_node
        if right_node:
            right_node = right_node.next
        reverse_tail.next = None
        # print(left_node,right_node)
        # print(reverse_head,reverse_tail)
        reverse_head = self.reverseList(reverse_head)
        if left_node:
            left_node.next = reverse_head
        else:
            head = reverse_head
        node = reverse_head
        while node.next:
            node = node.next
        node.next = right_node
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curNode = head
        while curNode:
            node = curNode.next
            curNode.next = new_head
            new_head = curNode
            curNode = node
        return new_head


if __name__ == '__main__':
    head = [1,2,3,4,5]
    left = 2
    right = 4
    print(LinkList(head))
    solution = Solution()
    node = solution.reverseBetween(LinkList(head).head,left,right)
    ll = []
    while node:
        ll.append(node.val)
        node = node.next
    print(ll)


