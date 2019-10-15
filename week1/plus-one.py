class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            i= -(i+1) 
            can_add = digits[i] != 9
            if can_add:
                digits[i] += 1 
                return digits
            
            else:
                digits[i] = 0
        return [1] + digits
        
                