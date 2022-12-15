from typing import List

# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 定义子问题为求解以某数结尾时，当前的最大和，定义一个数组保存这个结果
        # 对于每一个新的结果，如果签一个最大结果是负数或0，都没必要加，那么当前位置的最大结果是nums[i]本身
        if not nums:
            return 0
        sum_nums = []
        for idx,num in enumerate(nums):
            if idx == 0:
                sum_nums.append(num)
            else:
                last_sum = sum_nums[idx-1]
                sum_nums.append(num+max(0,last_sum))
        return max(sum_nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))