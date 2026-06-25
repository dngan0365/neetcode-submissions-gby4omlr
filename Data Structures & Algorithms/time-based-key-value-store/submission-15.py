class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        listKey = self.timeMap[key]
        print(listKey)
        l = 0
        r = len(listKey) - 1
        while l < r:
            mid = (l + r) // 2
            print("mid: ", mid, " ", listKey[mid][1])
            if listKey[mid][1] == timestamp:
                return listKey[mid][0]
            if listKey[mid][1] < timestamp:
                l = mid + 1
            else: 
                r = mid - 1
        print("left: ", l)
        if listKey[l][1] > timestamp:
            l -= 1
            if l >= 0:
                return listKey[l][0]
            else:
                return ""
        return listKey[l][0]
