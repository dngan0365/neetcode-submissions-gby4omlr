class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = []
        for w in strs:
            for c in w:
                b = str(ord(c)).zfill(3)
                final_str.append(b)
            final_str.append("#")
        print(final_str)
        return "".join(final_str)
            
    def decode(self, s: str) -> List[str]:
        prev = 0
        l_w = []
        for i in range(0, len(s)):
            if s[i] == "#":
                sub_str = s[prev:i]
                c = []
                for j in range(0, len(sub_str), 3):
                    a = int(sub_str[j:j+3])
                    b = chr(a)
                    c.append(b)
                w = "".join(c)
                prev = i+1
                l_w.append(w)
        return l_w


