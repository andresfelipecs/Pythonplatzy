class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if target == nums[i]+nums[j]:
                        return [i,j]
                    
                    
num = [1,2,3,4,5,6,7,8,9,10]
target = 8

s = Solution()
print(s.twoSum(num,target))