class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        k=0
        o=0
        count=0
        count2=0

        for i in range(len(nums)):
            if nums[k]==nums[i]:
                count+=1
                c=nums[k]
            
        for j in range(len(nums)):
            if nums[o]!=nums[i]:
                o=i
                if nums[o]==nums[j]:
                    count2+=1
                    d=nums[o]
                    break;
            break;

        if count>count2:
            return c
        else: return d



