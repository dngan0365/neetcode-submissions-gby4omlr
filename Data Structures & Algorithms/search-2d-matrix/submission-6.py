
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if target>matrix[i][n-1]:
                continue
            l, h = 0, n-1
            while l<=h:
                m = (l+h)//2
                if target==matrix[i][m]:
                    return True
                elif target<matrix[i][m]:
                    h = m-1
                else:
                    l = m+1
            return False
        return False






















# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         # find the row
#         row = -1
#         high, low = 0, len(matrix) -1
#         while high <= low:
#             mid = (high + low) // 2
#             if target >= matrix[mid][0] and target <= matrix[mid][-1]:
#                 row = mid
#                 break
#             if target > matrix[mid][-1]:
#                 high = mid + 1
#             elif target < matrix[mid][0]:
#                 low = mid - 1
#         if row == -1:
#             return False
        
#         l, r = 0, len(matrix[row])
#         while l <= r:
#             mid = (l+r)//2
#             if target == matrix[row][mid]:
#                 return True
#             elif target > matrix[row][mid]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return False