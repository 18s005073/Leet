import re
class Solution:
    def myAtoi(self, s):
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

if __name__ == '__main__':
    a = Solution()
    string = "-91283472332"
    print(a.myAtoi(string))