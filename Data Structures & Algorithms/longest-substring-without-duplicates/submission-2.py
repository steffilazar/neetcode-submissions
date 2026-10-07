class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen=set()
        l=0
        stg=0

        for r in range(len(s)):
            while s[r] in seen:
                stg=max(stg,r-l)
                
                seen.remove(s[l])
                l+=1 

            seen.add(s[r])
        return stg


























        # l=0
        # ans=0
        # seen=set()

        # for r in range(len(s)):

        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l+=1
        #     seen.add(s[r])
        #     ans=max(ans,r-l+1)

        # return ans

        