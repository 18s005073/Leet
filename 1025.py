import math
class Solution:
    def divisorGame(self,N):
        rsts = [False]*(N+1)
        for i in range(2,N+1):
            if i%2==0 and rsts[int(i/2)]==False:
                rsts[i] = True
                continue
            for j in range(1,int(math.sqrt(i))):
                if i%j==0:
                    if rsts[i-j] == False or (j!=1 and rsts[i-int(i/j)]==False):
                        rsts[i] = True
                        break
        return rsts[N]

if __name__ == '__main__':
    N = 8
    a = Solution()
    print(a.divisorGame(N))