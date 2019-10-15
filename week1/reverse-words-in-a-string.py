class Solution:
    def reverseWords(self, s: str) -> str:
        List = s.split()
        r = ""
        for i in range(len(List)):
            string = List[i]
            r+= string[len(string)::-1]+" "
        return r[:len(r)-1] 
            