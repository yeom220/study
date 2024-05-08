# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
import collections
import heapq
from typing import List

# Example 1:
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
expected = 700


# # Example 2:
# # Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# # Output: 200
# # Explanation:
# # The graph is shown above.
# # The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1
# expected = 200

# # Example 3:
# # Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# # Output: 500
# # Explanation:
# # The graph is shown above.
# # The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src = 0
# dst = 2
# k = 1
# expected = 500

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))
        print(graph)

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]

        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            print(Q)
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))

        return -1


s = Solution()
result = s.findCheapestPrice(n, flights, src, dst, k)
print(expected == result, result)
