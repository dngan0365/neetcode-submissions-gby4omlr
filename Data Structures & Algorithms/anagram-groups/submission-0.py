class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            key = tuple(sorted(s))  # tuple dùng làm key
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]

        return list(result.values())