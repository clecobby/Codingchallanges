class SumList:
    def sumlist(self, lst : list):
        if len(lst)==0:
            return 0
        else:
            return lst[0] + self.sumlist(lst[1:])
        
        
        

sumlist = SumList()
print(sumlist.sumlist([1,2,3,4,5,6]))