# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        token_dic = {"(":")","{":"}","[":"]"}
        stack = []
        for tok in s:
            if tok in token_dic:
                stack.append(tok)
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if token_dic[tmp] == tok:
                    continue
                else:
                    return False
        return False if stack else True


if __name__ == '__main__':
    solution = Solution()
    s = "()[]{"
    print(solution.isValid(s))