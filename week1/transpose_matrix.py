class Solution(object):

    def transpose(self, A):
        #assuming no jagged arrays 
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows = len(A)
        col = len(A[0]) 
        matrix = [[0 for x in range(rows)] for y in range(col)] 
        for r in range(rows):
            for c in range(col):
                matrix[c][r] = A[r][c]
                
        return(matrix)
 