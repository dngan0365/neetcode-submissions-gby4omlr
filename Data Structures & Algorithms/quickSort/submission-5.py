# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
# class Solution:
#     def quickSort(self, pairs: List[Pair]) -> List[Pair]:
#         return self.quickSortPair(pairs, 0, len(pairs)-1, 0+len(pairs) // 2)

#     def quickSortPair(self, pairs: List[Pair], l: int, r: int, pivot: int) -> List[Pair]:
#         if r - l + 1 == 0:
#             return pairs
#         pivot_pair = pairs[pivot]
#         curr_l = l
#         curr_r = r
#         while curr_l <= curr_r:
#             if pairs[curr_l].key > pivot_pair.key and pairs[curr_r].key < pivot_pair.key:
#                 temp = pairs[curr_l]
#                 pairs[curr_l] = pair[curr_r]
#                 pairs[curr_r] = temp
#                 curr_l += 1
#                 curr_r -= 1
#             if pairs[curr_l].key < pivot_pair.key:
#                 curr_l += 1
#             if pairs[curr_r].key > pivot_pair.key:
#                 curr_r -= 1

#         quickSortPair(pairs, l, curr_l, (l+curr_l)//2)
#         quickSortPair(pairs, curr_r, r, (r+curr_r)//2)
#         return pairs


# class Solution:
#     def quickSort(self, pairs: List[Pair]) -> List[Pair]:
#         if not pairs or len(pairs) <= 1:
#             return pairs
#         return self.quickSortPair(pairs, 0, len(pairs) - 1)

#     def quickSortPair(self, pairs: List[Pair], l: int, r: int) -> List[Pair]:
#         if l >= r:
#             return pairs

#         # Choose pivot (middle element)
#         # pivot_index = (l + r) // 2
#         pivot_index = r
#         pivot_value = pairs[pivot_index].key

#         i, j = l, r
#         while i <= j:
#             while pairs[i].key < pivot_value:
#                 i += 1
#             while pairs[j].key > pivot_value:
#                 j -= 1
#             if i <= j:
#                 pairs[i], pairs[j] = pairs[j], pairs[i]
#                 i += 1
#                 j -= 1

#         # Recursively sort both partitions
#         if l < j:
#             self.quickSortPair(pairs, l, j)
#         if i < r:
#             self.quickSortPair(pairs, i, r)

#         return pairs
class Solution:
    def quickSort(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # Base case: subarray of size 0 or 1
        if e - s + 1 <= 1:
            return pairs

        # Choose pivot (last element)
        pivot = pairs[e]
        left = s  # pointer for smaller elements

        # Partition: move smaller keys to the left
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        # Place pivot between left and right sides
        pairs[e], pairs[left] = pairs[left], pairs[e]

        # Recursively sort the two halves
        self.quickSort(pairs, s, left - 1)
        self.quickSort(pairs, left + 1, e)

        return pairs
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # Helper recursive function
        def sort(arr: List[Pair], s: int, e: int):
            if e - s + 1 <= 1:
                return

            # Choose pivot (last element)
            pivot = arr[e]
            left = s  # pointer for smaller elements

            # Partition
            for i in range(s, e):
                if arr[i].key < pivot.key:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1

            # Place pivot in the correct position
            arr[e], arr[left] = arr[left], arr[e]

            # Recurse on left and right halves
            sort(arr, s, left - 1)
            sort(arr, left + 1, e)

        # Start sorting the entire list
        sort(pairs, 0, len(pairs) - 1)
        return pairs
