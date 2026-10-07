class Solution:
    def isValid(self, s: str) -> bool:

        while s:
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')

        return s==''
        