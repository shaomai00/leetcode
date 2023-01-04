# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        newstr = ""
        jin = 0
        while i>=0 or j>=0 or jin:
            bitsum = jin
            if i>=0:
                bitsum += int(num1[i])
                i -= 1
            if j>=0:
                bitsum += int(num2[j])
                j -= 1
            jin = bitsum // 10
            bitsum = bitsum % 10
            newstr = str(bitsum) + newstr
        return newstr


if __name__ == '__main__':
    solution = Solution()
    print(solution.addStrings("123","11"))