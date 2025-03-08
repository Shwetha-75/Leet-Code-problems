class Solution:
    def traversalGraphDepthFirstSearch(self,edges:list[list[int]],vertices:int,source:int=0):
        
        adjacent=[[] for _ in range(vertices)]
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
        
       
        return self.visitedGraph([],[False]*(vertices),adjacent,1)
        
        
    def visitedGraph(self,result:list[int],visited:list[bool],adjacent:list[list[int]],source:int):
        visited[source]=True 
        result.append(source)
        for i in adjacent[source]:
            if not visited[i]:
                self.visitedGraph(result,visited,adjacent,i)
        
        return result

class TestApp:
        def testing_case_one(self):
            assert Solution().traversalGraphDepthFirstSearch([[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]],5,1)==[1,2,0,3,4]
         