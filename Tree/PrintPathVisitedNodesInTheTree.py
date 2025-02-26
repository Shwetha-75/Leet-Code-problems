# using DFS 
class Solution:
        def __init__(self):
            self.string=""
        def pathVisited(self,edges:list[list[int]],source:int):
            n=len(edges)
            visited=[False]*(n+1)
            adjacents=[[] for _ in range(n+1)]
            for edge in edges:
                print(adjacents)
                adjacents[edge[0]].append(edge[1])
                adjacents[edge[1]].append(edge[0])
            print(adjacents)
            self.printingPathVisited(source,visited,adjacents)
            print(self.string) 
        def printingPathVisited(self,source:int,visited:list[bool],adjacents:list[list[int]]):
            visited[source]=True 
            self.string+=str(source)+" "
            for adj in adjacents[source]:
                if not visited[adj]:
                       self.printingPathVisited(adj,visited,adjacents)
        
        


class TestApp:
        def testing_case_one(self):
        #     
        #                   0
        #                   |
        #                   1
        #                 /   \
        #                2     3 - 4 
        #           source : 0 
        #           path : 0 1 2 3 4
        #    
           sol=Solution()
           sol.pathVisited([[0,1],[1,2],[1,3],[3,4]],0)
           assert sol.string=="0 1 2 3 4 "
           
        def testing_case_two(self):
            #                 
            #                    0
            #               /    |     \
            #             1      2      3
            #           /   \   /  \   /  \
            #          4     5 6    7 8    9
            #         source: 4
            #         path: 4 0 1 5 3 8 9   
            sol=Solution()
            sol.pathVisited([[0,1],[0,4],[0,3],[1,4],[1,5],[2,6],[2,7],[3,8],[3,9]],4)
            assert sol.string=="4 0 1 5 3 8 9 "
# Solution().pathVisited([[0,1],[0,4],[0,3],[1,4],[1,5],[2,6],[2,7],[3,8],[3,9]],4)
Solution().pathVisited([[0,1],[1,2],[1,3],[3,4]],0)