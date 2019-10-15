class Solution(object):
    def sortArrayByParity(self, A):
        size = len(A)
        sortedA = [-1] * size
        front = 0 
        back = size -1
        
        for a in A:
            if (a % 2) == 0: 
                sortedA[front] = a
                front += 1 
            else:
                sortedA[back] = a 
                back-= 1 
        return sortedA