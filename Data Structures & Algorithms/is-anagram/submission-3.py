class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        ss={}
        tt={}

        for c in s:
            ss[c]= 1+ ss.get(c,0)
        for c in t:
            tt[c]=1+ tt.get(c,0)

        if ss==tt:
            return True
        else:
            return False