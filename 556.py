class Solution:
    def nextGreaterElement(self, n):
        num = n
        n = list(str(n))
        pos = leftMost = len(n) - 1
        for i in reversed(range(0, len(n) - 1)):
            if n[i] < n[i + 1]:
                leftMost = i
                break
        for i in reversed(range(leftMost + 1, len(n))):
            if n[i] > n[leftMost]:
                pos = i
                break

        n[leftMost], n[pos] = n[pos], n[leftMost]
        n[leftMost + 1:] = sorted(n[leftMost + 1:])
        n = int("".join(n))
        print
        n
        if n <= num or n > 0x7fffffff:
            return -1
        return n

if __name__ == '__main__':
    a = Solution()
    n = 91999
    b = a.nextGreaterElement(n)
    print(b)


