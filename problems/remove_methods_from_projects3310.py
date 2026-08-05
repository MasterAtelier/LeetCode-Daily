from collections import deque

class Solution:

    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:

        adj_list = [[] for _ in range(n)]
        for u , v in invocations:
  
            adj_list[u].append(v)

        queue = deque([k])
        suspicious = {k}
        while queue:
            current = queue.popleft()
            
            for neighbor in adj_list[current]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        for u,v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        return [method for method in range(n) if method not in suspicious]






        