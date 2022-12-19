# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0; j =0
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        new_list = []
        while i <m and j<n:
            if nums1[i]<=nums2[j]:
                new_list.append(nums1[i])
                i += 1
                if i == m:
                    new_list.extend(nums2[j:])
                    break
            else:
                new_list.append(nums2[j])
                j += 1
                if j == n:
                    new_list.extend(nums1[i:])
                    break
        nums1 = new_list
        return nums1

if __name__ == "__main__":
    solution = Solution()
    print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2= [2,5,6], n =3))