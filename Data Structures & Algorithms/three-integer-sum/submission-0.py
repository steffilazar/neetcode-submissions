class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
       

        for i,x in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l<r:
                summ=x+nums[l]+nums[r]
                if summ < 0:
                    l+=1
                elif summ>0:
                    r-=1
                else:
                    if [x,nums[l],nums[r]] not in res:
                        res.append([x,nums[l],nums[r]])
                    l+=1
                    r-=1
                    
            
        return res

