class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{',']':'[',')':'('}
        stackS = []
        for c in s:
            if c in closeToOpen:
                if stackS and stackS[-1] == closeToOpen[c]:
                    stackS.pop()
                else:
                    return False
            else:
                stackS.append(c)
        return True if not stackS else False