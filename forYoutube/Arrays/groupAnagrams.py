from collections import defaultdict
class Solution:
    
    def groupAnagrams(self,strs:list[str])->list[list[str]]:
        res= defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s) 
        return res.values()
    
    
if __name__== "__main__":
    solution= Solution()
    results= solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])
    print(results)