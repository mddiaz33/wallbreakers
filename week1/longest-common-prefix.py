class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        pfx= strs[0]
        for st in strs:
            if len(st) < len(pfx):
                pfx = pfx[:len(st)]
            for i in range(len(st)):
                keep_going = i < min(len(pfx), len(st))
                if(keep_going and pfx[i] != st[i]):
                    pfx = st[:i]
        return pfx