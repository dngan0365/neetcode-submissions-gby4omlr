class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in nums:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1

        # get sorted list of frequencies
        val = list(temp.values())
        val.sort()

        # get top k frequencies
        final_val = set(val[-k:])

        res = []
        for i in temp.keys():
            if temp[i] in final_val:
                res.append(i)

        return res
