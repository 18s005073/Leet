class Solution:
    def toLowerCase(self, str):
        s = ''
        for i in str:
            if 'A' <= i <= 'Z':
                s += chr(ord(i)+32)
            else:
                s += i
        return s

if __name__ == '__main__':
    a = Solution()
    string = 'Hello'
    print(a.toLowerCase(string))
