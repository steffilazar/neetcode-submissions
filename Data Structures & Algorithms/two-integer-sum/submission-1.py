class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        listt=list()

        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[i]+nums[j+1]==target:
                    listt.append(i)
                    listt.append(j+1)
                    return listt
                
