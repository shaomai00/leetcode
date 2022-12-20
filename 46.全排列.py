# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
from typing import List
class Solution:
    def permute_part(self, nums, tmp_res):
        if not nums:
            self.res.append(tmp_res)
            return
        for i in range(len(nums)):
            cur_num = nums[i]
            # tmp_res + cur_num
            self.permute_part(nums[:i]+nums[i+1:],tmp_res+[cur_num])
            # tmp_res - cur_num

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.permute_part(nums,[])
        return self.res




if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print(solution.permute(nums))