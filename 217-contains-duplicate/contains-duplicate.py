class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        nums.sort()        
        
        pre = nums[0]

        for i in range(1, len(nums)):
            if(pre == nums[i]): return True
            pre = nums[i]

        return False
            