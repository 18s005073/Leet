class Solution:
    def twoSum(self, nums, target):
        d = {}
        for key, value in enumerate(nums):
            if target-value in d:
                return [d[target-value],key]
            d[value] = key

if __name__ == '__main__':
    a = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    l = a.twoSum(nums,target)
    print(l)