class Solution:
    def romanToInt(self, s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = s[::-1]
        num = d[s[0]]
        for i in range(1,len(s)):
            if d[s[i]]<d[s[i-1]]:
                num -= d[s[i]]
            else:
                num += d[s[i]]
        return num

if __name__ == '__main__':
    s = "MCMXCIV"
    a = Solution()
    print(a.romanToInt(s))