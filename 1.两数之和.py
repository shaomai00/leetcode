from typing import List
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

class Solution:
    # 哈希法，空间占用高，时间复杂度O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个字典 存储{num: index}
        d = {}
        # 遍历数组中的每个数字
        for i,num in enumerate(nums):
            # 如果目标值减去当前值在字典中，说明找到了这两个数字，返回相应的下表即可
            if target - num in d:
                return [i, d[target-num]]
            # 将当前数字的下标存进字典
            d[num] = i
        return [-1,-1]


    # 暴力解法
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            if i == len(nums)-1:
                return []
            for j, num2 in enumerate(nums[i+1:]):
                j = i + 1 + j
                if num + num2 == target:
                    return [i,j]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum2(nums = [2,7,11,15], target = 9))