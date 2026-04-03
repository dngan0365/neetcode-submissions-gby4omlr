import copy

# # Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# class Solution:
#     def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
#         history = [copy.deepcopy(pairs)]
#         n = len(pairs)
#         print(n)
#         for i in range(1, len(pairs)):
#             j = i 
#             print(i)
#             print(pairs[j].key, " ", pairs[j-1].key)
#             while j > 0 and pairs[j].key > pairs[j-1].key:
#                 temp = pairs[j-1]
#                 pairs[j-1] = pairs[j]
#                 pairs[j] = temp
#                 j -= 1

#             history.append(copy.deepcopy(pairs))
#             print(pairs[:])

#         return history

from typing import List
import copy

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, '{self.value}')"

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        history = []
        n = len(pairs)
        if n == 0: 
            return history

        history.append(pairs[:])

        for i in range(1, n):
            j = i
            # Move left while current key < previous key (ascending order)
            while j > 0 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            history.append(pairs[:])
        return history
