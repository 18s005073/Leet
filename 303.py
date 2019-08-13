# class NumArray:
#     def __init__(self,nums):
#         self.dp = [0]*(len(nums))
#         self.dp[0] = nums[0]
#         for i in range(1,len(nums)):
#             self.dp[i] = self.dp[i-1]+nums[i]
#     def sumRange(self,i,j):
#         return (self.dp[j]-self.dp[i-1]) if (i-1)>=0 else self.dp[j]
#
# if __name__ == '__main__':
#     nums = [1,5,2,4,7,4,8]
#     a = NumArray(nums)
#     print(a.sumRange(0,4))

