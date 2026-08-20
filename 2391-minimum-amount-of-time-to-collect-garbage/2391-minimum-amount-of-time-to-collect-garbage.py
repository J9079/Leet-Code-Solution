class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        total = 0
        for house in garbage:
            total += len(house)
        last_M = -1
        last_P = -1
        last_G = -1
        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                last_M = i
            if 'P' in garbage[i]:
                last_P = i
            if 'G' in garbage[i]:
                last_G = i
        if last_M > 0:
            total += travel[last_M - 1]
        if last_P > 0:
            total += travel[last_P - 1]
        if last_G > 0:
            total += travel[last_G - 1]
        return total