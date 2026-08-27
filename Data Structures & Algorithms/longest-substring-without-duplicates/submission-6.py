class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        grp=set()
        l=0
        res=0

        for r in range(len(s)):
            while s[r] in grp:
                grp.remove(s[l])
                l+=1
            else:
                grp.add(s[r])
            res=max(res,r-l+1)

        return res




























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

        