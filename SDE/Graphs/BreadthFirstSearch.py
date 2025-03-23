class Solution:
      def bfsTraversal(self,edges:list[list[int]],vertices:int):
            adjacent=[[] for _ in range(vertices)]
            for edge in edges:
                adjacent[edge[0]].append(edge[1])
                adjacent[edge[1]].append(edge[0])
            
            queue=[0]
            visited=[False for _ in range(vertices)]
            result=[]
            visited[0]=True 
            while queue:
                    node=queue.pop(0)
                    result.append(node)
                    for adj in adjacent[node]:
                       if not visited[adj]:
                           visited[adj]=True 
                           queue.append(adj)
            return result 
             
class TestApp:
      def testing_case_one(self):
          assert Solution().bfsTraversal([[1,2],[1,0],[2,0],[2,3],[2,4]],5)==[0,1,2,3,4]
      def testing_case_two(self):
          assert Solution().bfsTraversal([[1,0],[0,2],[0,3],[2,3],[2,4]],5)==[0,1,2,3,4]

