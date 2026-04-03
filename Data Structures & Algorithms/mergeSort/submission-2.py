# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        if n <= 1:
            return pairs
        m = n // 2
        L = pairs[0:m]
        R = pairs[m:n]
        sort_L = self.mergeSort(L)
        sort_R = self.mergeSort(R)
        sort_arr = self.merge(pairs, sort_L, sort_R)
        return sort_arr

    def merge(self, arr: List[Pair], sort_L: List[Pair], sort_R: List[Pair]) -> List[Pair]:
        l = 0
        r = 0
        k = 0
        n_l = len(sort_L)
        n_r = len(sort_R)
        while l < n_l and r < n_r:
            if sort_L[l].key <= sort_R[r].key:
                arr[k] = sort_L[l]
                l += 1
                k += 1
            else:
                arr[k] = sort_R[r]
                r += 1
                k+=1
        
        while l < n_l:
            arr[k] = sort_L[l]
            l += 1
            k += 1
        
        while r < n_r:
            arr[k] = sort_R[r]
            r += 1
            k += 1
        return arr
