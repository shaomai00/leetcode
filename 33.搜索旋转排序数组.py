# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 时间复杂度O(logn)

# 将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
# 此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:  # 等于targe的已经返回了，下面都不用考虑这种情况
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,8,1,2,3]
    solution = Solution()
    print(solution.search(nums,target=8))
