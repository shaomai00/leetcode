# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度
class Solution:
    # 方案一和方案二是一样的效率
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 空字符串直接返回0
        if not len(s):
            return 0
        # max_length变量保存最大的字串长度
        max_length = 1
        # 头指针，尾指针 确定片段
        i = 0; j = i + 1
        # set保存当前片段中的独立字符
        span_set = set(s[i])
        while j < len(s):
            # 没有重复时就添加
            if s[j] not in span_set:
                span_set.add(s[j])
                max_length = max(max_length, len(span_set))
                j += 1
            # 有重复时从头指针开始推出，直到推到当前这个字符
            else:
                for offset in range(i,j):
                    if s[offset] == s[j]:
                        span_set.remove(s[offset])
                        i = offset + 1       # 头指针指向重复的下一位
                        span_set.add(s[j])
                        j += 1               # 尾指针指向下一位
                        break
                    else:
                        span_set.remove(s[offset]) # 从头指针持续推出
        return max_length
    # 方法二
    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 创建一个字典用来存储当前字符最后一次出现的位置
        if not s:
            return 0
        d = {}
        max_length = 1
        start = 0
        for idx, num in enumerate(s):
            # 如果当前字符在字典中，并且它的最近一次出现位置在当前无重复字符的最长子串的开始位置之后，更新无重复字符的最长子串的开始位置
            if num in d and start <= d[num]:
                start = d[num] + 1
            # 更新当前字符的最近一次出现位置
            d[num] = idx
            # 更新无重复字符的最长子串的长度
            max_length = max(max_length, idx - start + 1)
        return max_length

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring2(s = "qrsvbspk"))
    print(solution.lengthOfLongestSubstring2(s="bbbb"))
    print(solution.lengthOfLongestSubstring2(s="pwwkew"))
    print(solution.lengthOfLongestSubstring2(s="tmmzuxt"))