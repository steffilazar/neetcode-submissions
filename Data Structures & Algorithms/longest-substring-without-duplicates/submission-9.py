class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        
        seq=set()
        leng=0

        for r in range(len(s)):
            while s[r] in seq:
                seq.remove(s[l])
                l+=1
            seq.add(s[r])
            leng=max(leng,r-l+1)
        return leng
