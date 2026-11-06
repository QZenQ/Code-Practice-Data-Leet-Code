class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        al = [[] for _ in range(n)]

        for u, v in edges:
            al[u].append(v)
            al[v].append(u)

        visited = set()
        Q = []
        Q.append(source)
        visited.add(source)
        
        while(len(Q) > 0):
            cn = Q.pop(0)

            if cn == destination:
                return True

            

            for node in al[cn]:
                if(node not in visited):
                    Q.append(node)
                    visited.add(node)


        return False
