# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
import collections
from typing import List

# # Example 1:
# # Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# # Output: ["JFK","MUC","LHR","SFO","SJC"]
# input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]


# Example 2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
input = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # # 1. DFS로 일정 그래프 구성
        # graph = collections.defaultdict(list)
        # for a, b in sorted(tickets):
        #     graph[a].append(b)
        # print(graph)

        # route = []
        #
        # def dfs(a):
        #     while graph[a]:
        #         r = graph[a].pop(0)
        #         print('pop=', r)
        #         dfs(r)
        #     route.append(a)
        #
        # dfs('JFK')
        # return route[::-1]

        # # 2. 스택 연산으로 큐 연산 최적화 시도
        # graph = collections.defaultdict(list)
        # for a, b in sorted(tickets, reverse=True):
        #     print('a, b', a, b)
        #     graph[a].append(b)
        #
        # print(graph)
        # route = []
        #
        # def dfs(a):
        #     while graph[a]:
        #         r = graph[a].pop()
        #         print('pop=', r)
        #         dfs(r)
        #     route.append(a)
        #
        # dfs('JFK')
        # return route[::-1]

        #3. 일정 그래프 반복
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            print('a, b', a, b)
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            print('stack=', stack)
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                g_pop = graph[stack[-1]].pop(0)
                print('g_pop=', g_pop)
                stack.append(g_pop)

            s_pop = stack.pop()
            print('s_pop=', s_pop)
            route.append(s_pop)
            print('route=', route)

        return route[::-1]


s = Solution()
result = s.findItinerary(input)
print(expected == result, result)
