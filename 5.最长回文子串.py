

class Solution:
    # 暴力法：遍历所有可能，从大的开始遍历  时间复杂度 O(n^3)
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        for window_size in range(len(s),1,-1):
            for start_index in range(len(s) - window_size + 1):
                piece = s[start_index:start_index+window_size]
                if piece == piece[::-1]:
                    return piece
        return s[0]
    # 回文意味着以某一位为中心点，向两边扩散都一样，当piece为奇数位时，中心点是一个字符。当piece为偶数位时，中心点是两个字符。
    # 分别进行假设，寻找可能的最远端
    # 时间复杂度 O(n^2)
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return ""
        final_left = final_right = 0
        for idx in range(len(s)-1):
            # 奇长情况
            left = right = idx
            # 因为left还要再-1,所以条件要保证left > 0，而不是>=0
            while s[left] == s[right]:
                if right - left > final_right - final_left:
                    final_right, final_left = right, left
                if left > 0 and right < len(s) - 1:
                    left -= 1
                    right += 1
                else:
                    break
            # 偶长情况
            left = idx
            right = idx + 1
            while s[left] == s[right]:
                if right - left > final_right - final_left:
                    final_right, final_left = right, left
                if left > 0 and right < len(s) - 1:
                    left -= 1
                    right += 1
                else:
                    break
        return s[final_left:final_right+1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome2("aaba"))