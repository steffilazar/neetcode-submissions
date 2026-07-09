class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        listt=list()
        n=1

        for i in range(len(nums)):
            for j in range(len(nums)-n):
                if nums[i]+nums[j+n]==target:
                    listt.append(i)
                    listt.append(j+n)
                    return listt
            n+=1    
                    
                
