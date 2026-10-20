class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        ss={}
        tt={}
        for c in range(len(s)):
            ss[s[c]]=1+ss.get(s[c],0)
            tt[t[c]]=1+tt.get(t[c],0)
        return ss==tt
            
