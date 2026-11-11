class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        dC = [[] for i in range(numCourses)]
        ind = [0] * numCourses

        for u, v in prerequisites:
            dC[v].append(u)
            ind[u] += 1
        
        Q = [i for i in range(numCourses) if ind[i] == 0]
        result = []

        while Q:
            cn = Q.pop(0)
            result.append(cn)

            for node in dC[cn]:
                ind[node] -= 1

                if(ind[node] == 0):
                    Q.append(node)
                    
        if(len(result) == numCourses):
            return result

        return []