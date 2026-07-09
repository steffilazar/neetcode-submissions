class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=='': return ''

        countt, window ={}, {}
        reslen=float('inf')
        res=[-1,-1]

        for i in t:
            countt[i] = 1 +countt.get(i,0)

        have, need= 0, len(countt)
        l=0

        for r in range(len(s)):
            c=s[r]
            window[c] = 1 + window.get(c,0)

            if c in countt and window[c]==countt[c]:
                have+=1

            while have==need:
                #update res
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                
                window[s[l]]-=1
                if s[l] in countt and window[s[l]]<countt[s[l]]:
                    have-=1
                l+=1 
        
        l,r=res

        return s[l:r+1] if reslen!=float('inf') else ''
            
            



        