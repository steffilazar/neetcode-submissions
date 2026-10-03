class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dup={}

        for i,n in enumerate(nums):
            need=target - nums[i]
            if need in dup:
                return [dup[need],i]
            dup[n]=i