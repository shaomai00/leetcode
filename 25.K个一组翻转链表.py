from __future__ import annotations
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
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
        # return str(self.head.val)
class Solution:
    # 自己写的，一次通过，把每k个反转后的head放在list里，最后再遍历一遍list给连起来
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur_node = head
        new_tmp_list = []
        while cur_node:
            # 判断剩下的有没有k个
            remain_cnt = 1
            tmp_node = cur_node
            while tmp_node.next:
                remain_cnt += 1
                tmp_node = tmp_node.next
                if remain_cnt == k:
                    break
            if remain_cnt < k: # 如果不到k个就返回了
                new_tmp_list.append(cur_node)
                break
            else:  # 如果够，就对连续的k个进行翻转，并且注意，如果是第一次翻转之前，得把reversed_list_head 置空，不然还连着之前的
                reversed_list_head = None
                for i in range(k):
                    node = cur_node.next
                    cur_node.next = reversed_list_head
                    reversed_list_head = cur_node
                    cur_node = node
                new_tmp_list.append(reversed_list_head)
        if len(new_tmp_list) == 1:
            return new_tmp_list[0]
        for idx, node in enumerate(new_tmp_list[:-1]):
            while node.next:
                node = node.next
            node.next = new_tmp_list[idx+1]
        return new_tmp_list[0]


if __name__ == '__main__':
    solution = Solution()
    l1 = LinkList([1, 2, 3, 4, 5])
    print(solution.reverseKGroup(l1.head,k=2))