class Solution:
    def uniqueMorseRepresentations(self, words):
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
             ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--","-..-","-.--","--.."]
        l = []
        for i in words:
            s = ''
            for j in i:
                s += d[ord(j)-ord('a')]
            l.append(s)
        set_l = set(l)
        return len(set_l)

if __name__ == '__main__':
    a = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(a.uniqueMorseRepresentations(words))


