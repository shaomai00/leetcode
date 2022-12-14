# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
# 请你返回所有和为 0 且不重复的三元组
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   # 两层循环，时间复杂度On2
        if len(nums)<3:
            return []
        result = []
        nums.sort() # nlogn
        for idx in range(len(nums)-2): # 随着第一个元素的递增，第二个元素是递减的，那么就可以使用双指针的方法，将枚举的时间复杂度从 O(N2)减少至 O(N)
            a_num = nums[idx]
            if idx>0 and nums[idx-1]==a_num: # 需要和上一次枚举的值不同
                continue
            target = -a_num
            kdx = len(nums) - 1
            for jdx in range(idx+1, len(nums)-1):
                b_num = nums[jdx]
                if jdx > idx+1 and nums[jdx-1] == b_num:  # 需要和上一次枚举的值不同
                    continue
                while jdx < kdx and b_num + nums[kdx] > target:
                    kdx -= 1
                if jdx == kdx:
                    break
                if b_num + nums[kdx] == target:
                    result.append([a_num,b_num,nums[kdx]])
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
