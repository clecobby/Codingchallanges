class Solution :
    
    def validParenthesis(self, s:str)->bool:
        Map = {")":"(","]":"[","}":"{"}
        stack = []
        
        for c in s: 
            if c in Map:
                if stack and stack[-1]==Map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not  stack else False
                







if __name__=="__main__":
    solution = Solution()
    results=solution.validParenthesis('[](){}')
    print(results)