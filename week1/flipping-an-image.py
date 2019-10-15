class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        size = len(A)
       #empty list for return matrix
        r = []
        # loop through each row in A 
        for x in A:
        # reverse elements 
            x.reverse()
        #call to invert bits 
            r.append(self.invertRow(x))
        return r
    
    #returns inverse of reversed row 
    def invertRow(self, row: List[int]) -> List[int]:
        for i in range(len(row)):
            
            row[i] = abs(row[i] -1)
                
        return row