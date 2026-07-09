class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x, y = 0, 0
        s = ""

        if len(word1)<len(word2):
            for x in range(len(word1)):
                s+=(word1[x])
                s+=(word2[y])
                x+=1
                y+=1
            s+=(word2[y:])

        
        if len(word1)>len(word2):
            for x in range(len(word2)):
                s+=(word1[x])
                s+=(word2[y])
                x+=1
                y+=1
            s+=(word1[x:])

        if len(word1)==len(word2):
            for x in range(len(word1)):
                s+=(word1[x])
                s+=(word2[y])
                x+=1
                y+=1

        return s
            
        

