class Solution:
    def convert(self, s, numRows):
        if len(s)<=numRows or numRows == 1:
            return s
        b = 2*(numRows-1)
        a = s[::b]
        for i in range(1,numRows-1):
            flag = True
            index = i
            while index<len(s):
                a += s[index]
                index += b-(2*i) if flag else 2*i
                flag = not flag
        a += s[numRows-1::b]
        return a

if __name__ == '__main__':
    a = Solution()
    s = "AB"
    numRows = 1
    print(a.convert(s,numRows))