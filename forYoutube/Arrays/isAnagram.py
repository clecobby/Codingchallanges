class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countforS, countforT = {},{}
        for i in range(len(s)):
            countforS[s[i]]=1+ countforS.get(s[i],0)
            countforT[t[i]]=1+ countforT.get(t[i],0)
        return countforS==countforT