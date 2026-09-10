class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        buffer = None
        cu = 0
        for i in range(len(nums)):
            if(buffer != nums[i]):
                buffer = nums[i]
                nums[cu] = nums[i]
                cu +=1
                continue
            
                
        nums[:] = nums
        return cu
            
            