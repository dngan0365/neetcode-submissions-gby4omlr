class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_length = max(heights)
        # print(max_length)
        max_volume = 0
        n = len(heights)
        for i in range(max_length, -1, -1):
            width = 0
            print(i)
            for j in range(0, n+1):
                if j < n and heights[j] >= i:
                    width += 1
                else:
                    curr = i * width
                    # print(curr)
                    if curr > max_volume:
                        print(i, " ", width)
                        max_volume = curr
                    width = 0
        return max_volume
