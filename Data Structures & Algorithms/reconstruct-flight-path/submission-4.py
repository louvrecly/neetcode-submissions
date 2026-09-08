class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # [A -> B]
        # [A -> C]
        # [B -> A]
        # [C -> D]
        # [C -> F]
        # [D -> E]
        # [E -> C]

        # A: (2 1) ->  1
        # B: (1 1) ->  0
        # C: (2 2) ->  0
        # D: (1 1) ->  0
        # E: (1 1) ->  0
        # F: (0 1) -> -1
        # A: [B C]
        # B: [A]
        # C: []
        #    A
        #  // \
        # B    C - F
        #     / \
        #    D - E
        # Hierholzer's Algorithm -> Find Eulerian Path
        # Time: O(E) | Space: O(E)
        tickets.sort(reverse=True)
        adj = defaultdict(list)

        for depart, land in tickets:
            adj[depart].append(land)

        stops = deque([])
        def dfs(stop: str) -> None:
            while adj[stop]:
                nextStop = adj[stop].pop()
                dfs(nextStop)
            stops.appendleft(stop)

        dfs('JFK')
        return list(stops)
        # tickets.sort()
        # adj = defaultdict(list)

        # for depart, land in tickets:
        #     adj[depart].append(land)

        # stops = ['JFK']

        # def dfs(stop: str) -> bool:
        #     if len(stops) == len(tickets) + 1:
        #         return True
        #     if not adj[stop]:
        #         # return len(stops) == len(tickets) + 1
        #         return False

        #     nextStops = list(adj[stop])
        #     for i, nextStop in enumerate(nextStops):
        #         stops.append(nextStop)
        #         adj[stop].pop(i)
        #         if dfs(nextStop):
        #             return True

        #         stops.pop()
        #         adj[stop].insert(i, nextStop)
            
        #     return False

        # dfs('JFK')
        # return stops
