from typing import List,Optional
# list大小为k，如果直接遍历合并，则越合并越长，时间复杂度为O((1+k)*k/2 * n)=O(k^2n)
# 如果分治法，2个2个合并，O(kn×logk)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkList:
    def __init__(self, nums):
        if not nums:nums=[0]
        self.head = ListNode(nums[0])
        node = self.head
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next
    def __repr__(self):
        res = []
        node = self.head
        while node:
            res.append(node.val)
            node = node.next
        return str(res)

class Solution:
    def merge2List(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        head = ListNode()
        node = head
        while head1 and head2:
            if head1.val <= head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        if head1:
            node.next = head1
        if head2:
            node.next = head2
        return head.next
    def merge(self,list, start, end):
        if start == end:
            return list[start]
        mid = start + (end - start) // 2
        l1 = self.merge(list, start, mid)
        l2 = self.merge(list, mid+1, end)
        return self.merge2List(l1,l2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.merge(lists, 0, len(lists)-1)


if __name__ == '__main__':
    solution = Solution()
    ll = []
    for i in [[],[-1,5,11],[],[6,10]]:
        ll.append(LinkList(i).head)
    print(solution.mergeKLists(ll).val)
