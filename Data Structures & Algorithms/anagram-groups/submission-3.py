class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # for s in strs:
        #     key = tuple(sorted(s))  # tuple dùng làm key
        #     if key in result:
        #         result[key].append(s)
        #     else:
        #         result[key] = [s]

        # return list(result.values())

        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())
