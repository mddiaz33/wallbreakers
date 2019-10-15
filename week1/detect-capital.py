import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return len(re.sub("^[A-Z]{1}[a-z]+$|^[a-z]+$|^[A-Z]+$", "", word)) == 0