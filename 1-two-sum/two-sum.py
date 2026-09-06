class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}

        for i in range(len(nums)):

            if target - nums[i] in freq:
                return [i, freq[target - nums[i]]]

            freq[nums[i]] = i


            