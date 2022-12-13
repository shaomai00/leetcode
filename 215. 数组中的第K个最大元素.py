# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
import heapq
from typing import List
import random

# def partition(array, l ,r):
#     for i in range(l,r):
#         2
class Solution:
    # topK快排算法成为快速选择，在快排Onlogn的时间内，可以进一步缩短时间
    # 假设pivot_index小于k，不用再递归左半边，只在右半边继续递归即可
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        while 1:
            pivot_idx = random.randint(low, high)  # 随机选择pivot，和low位置交换，降低平均时间复杂度
            nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low] # 这两行不要也行
            pi = self.partition_reverse(nums, low, high)
            if pi == k-1:
                return nums[pi]
            elif pi < k-1: # 说明目标在右侧
                low = pi + 1
            else:
                high = pi - 1
    def partition_reverse(self, nums, low, high): # 逆序排，high的位置放小数，low的位置放大数
        # pivot_idx = random.randint(low, high) 可不能在这里随机选，因为下面high,low位置的赋值，都是相当于在往空位置放数字，默认初始情况下左边是空位置
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] <= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] > pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    def partition(self,nums,low,high): # 返回参考点最终的索引
        pivot = nums[low]
        while low < high:
            # high是从右向左走，如果值大于pivot则位置保持不变，j左移
            while low < high and nums[high] >= pivot:
                high -= 1
            # 不满足上述条件时，nums[high]<pivot,应该放在左边，所以将low位置赋值为high
            # 此时high位置空出
            nums[low] = nums[high]
            # low 从左向右走，如果值小于pivot则位置不变，low右移
            while low < high and nums[low] < pivot:
                low += 1
            # 不满足上述条件时，nums[low]>=pivot,应该放在右边，所以将high位置赋值为low
            # 此时low位置空出
            nums[high] = nums[low]
        # 将pivot的值放到正确的索引位置
        nums[low] = pivot
        return low

    # quickSort才是递归的中心
    def quickSort(self,nums: List[int], low, high):
        if len(nums)<=1:
            return nums
        if low < high:
            pi = self.partition(nums,low,high)
            self.quickSort(nums,low,pi-1)
            self.quickSort(nums,pi+1,high)
        return nums

    # 堆排序解决这个问题,建立一个大根堆，做 k−1 次删除操作后堆顶元素就是我们要找的答案
    # 时间复杂度：O(nlogn)，建堆的时间代价是O(n)，删除的总代价是 O(klogn)，因为k<n，故渐进时间复杂为O(n+klogn)=O(nlogn)
    import heapq
    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
        for _ in range(k-1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]

    # 手撸堆
    def findKthLargestHeapManual(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 建堆，大顶堆
        self.buildMaxHeap(nums)
        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        for i in range(k - 1):
            nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
            self.adjust_down(nums, 0, n - 1 - i - 1)
        return nums[0]

    def buildMaxHeap(self,nums):
        for root in range(len(nums)//2-1 , -1, -1): # 遍历所有非叶子节点，第一个非叶子结点是n//2-1
            self.adjust_down(nums, root, len(nums)-1)

    def adjust_down(self, nums, root, end):
        child = 2*root + 1 # 左子节点, 右子节点：child+1
        while child <= end:
            if child+1 <=end and nums[child+1] > nums[child]: #取两者中大的
                child += 1 # child指向两者中大的一个
            if nums[root] < nums[child]:  # 如果根节点小，就要交换调整，让大的保持在堆顶
                nums[root], nums[child] = nums[child], nums[root]
                root = child    # 继续往下，判断顺序遵循从上到下，从左到右
                child = 2*root + 1
            else:
                break


if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargestHeapManual([3,2,3,1,2,4,5,5,6],k=4))
    # print(solution.quickSort([3,2,1,5,6,4],0,5))