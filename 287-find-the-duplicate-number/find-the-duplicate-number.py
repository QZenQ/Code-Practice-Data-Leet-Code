class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hp = 0
        tp = 0
        while True:
            hp = nums[nums[hp]]
            tp = nums[tp]

            if(tp == hp):                
                break

        tp = 0
        while True:
            if(nums[tp] == nums[hp]): return nums[tp]
            tp = nums[tp]
            hp = nums[hp]

            


