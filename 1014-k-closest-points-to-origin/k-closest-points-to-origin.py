import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointMap = {}
        pointArray = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            # pointMap[distance] = point
            if distance in pointMap:
                pointMap[distance].append(point)
            else:
                pointMap[distance] = [point]
            pointArray.append(distance)
        
        heapq.heapify(pointArray)
        res = []
        
        i = 0
        while i < k:
            min = heapq.heappop(pointArray)
            subArr = pointMap.get(min)
            for coordinate in subArr:
                res.append(coordinate)
                i += 1
        return res