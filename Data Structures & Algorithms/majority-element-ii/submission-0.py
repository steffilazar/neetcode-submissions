class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res=[]
        count={}
        n=len(nums)

        for num in nums:
            count[num]=count.get(num,0)+1
            if count[num]>n/3 and num not in res:
                res.append(num)
        return res
        