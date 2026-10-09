class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        i=0
        def bt(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            if i==len(nums):
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                bt(path)
                path.pop()

        bt(path)
        return res
