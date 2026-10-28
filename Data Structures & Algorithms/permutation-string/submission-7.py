class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)

        one=Counter(s1)
        two=Counter(s2[l:r])

        while r<len(s2):
            
            if one==two:
                return True
            
            two[s2[l]]-=1
            if two[s2[l]]==0:
                del two[s2[l]]

            two[s2[r]]+=1

            
            l+=1
            r+=1
        return one==two
