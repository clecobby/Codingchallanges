class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(","]":"[","}":"{"}
        stack= []
        for c in s:
            if c not in Map:
                stack.append(c)
                print (f"****{c}")
                continue
            if not stack or stack[-1] != Map[c]:
                print (f"****%%%{c}")
                return False
            stack.pop()
        print (f"2323")
        return not stack
    
if __name__=="__main__":
    solution = Solution()
    results=solution.isValid('[)(]')
    print(results)