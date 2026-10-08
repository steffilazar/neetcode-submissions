class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        path=[]

        def bt(i,path):
            
            if i==len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            bt(i+1,path)

            path.pop()
            bt(i+1,path)
        bt(0,path)
        return res