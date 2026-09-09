class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        x = 0
        flag = 0
        while x < len(s):
            j = x
            while s[j].isdigit():
                j += 1
            length = int(s[x:j])
            res.append(s[j+1:j+length+1])
            x = j + length + 1
            print(x)
        return res