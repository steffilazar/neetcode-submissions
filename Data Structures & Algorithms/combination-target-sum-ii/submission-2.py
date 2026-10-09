class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        path=[]
        res=[]
        candidates.sort()

        def bt(i,remaining):
            if remaining==0:
                res.append(path[:])
                return
            if remaining<0 or i==len(candidates):
                return
            path.append(candidates[i])
            bt(i+1,remaining-candidates[i])
            path.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1

            bt(i+1,remaining)
        bt(0,target)
        return res