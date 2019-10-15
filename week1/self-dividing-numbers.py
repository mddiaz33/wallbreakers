class Solution:
    memo = set()
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        List =[]
        return  self.selfDividingRecursion(left,right,List )
        
    
    def selfDividingRecursion(self, start:int, end: int, List: List[int] ) ->  List[int]:
        if start > end: 
            return List
        elif start in self.memo:
            List.append(start)
        else:
            isSelfDividing = True
            for i in str(start):
                if int(i) == 0 or start % int(i) != 0:
                    isSelfDividing = False
            if isSelfDividing: 
                self.memo.add(start)
                List.append(start)
        return self.selfDividingRecursion( start+1, end, List )
                
                