class Solution(object):
   def twoSum(self, nums, target):
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i
input_list = [1, 2, 3]
ob1 = Solution()
print(ob1.twoSum(input_list, 4))


# twoSum([1, 2, 3], 4)        # [0, 2]
# twoSum([2, 7, 11, 15], 9)   # [0, 1]
# twoSum([3, 2, 4], 6)        # [1, 2]
# twoSum([3, 3], 6)           # [0, 1]