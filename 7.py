class Solution:
    def reverse(self, x):
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        return sign * ans if ans <= 0x7fffffff else 0

if __name__ == '__main__':
    x = 123
    a = Solution()
    print(a.reverse(x))


