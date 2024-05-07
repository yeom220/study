# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
import collections
import heapq
from typing import List

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
expected = 2


# # Example 2:
# # Input: times = [[1,2,1]], n = 2, k = 1
# # Output: 1
# times = [[1,2,1]]
# n = 2
# k = 1
# expected = 1

# # Example 3:
# # Input: times = [[1,2,1]], n = 2, k = 2
# # Output: -1
# times = [[1,2,1]]
# n = 2
# k = 2
# expected = -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 다익스트라 알고리즘 구현
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        print('graph=', graph)

        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선순튀 큐 최솟값을 기준으로 정점까지 최단 경로 삽입
        while Q:
            print('Q=', Q)
            print('dist=', dist)
            time, node = heapq.heappop(Q)
            print('time, node', time, node)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1


s = Solution()
result = s.networkDelayTime(times, n, k)
print(expected == result, result)
