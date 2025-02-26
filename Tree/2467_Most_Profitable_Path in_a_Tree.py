from collections import deque
import sys
class Solution:
    def __init__(self):
        self.visited_bob=[]
        self.visited_alice=[]
        self.bob_path={}
        self.adjacent_nodes=[]
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n=len(amount)
        self.visited_bob=[False]*n 
        self.visited_alice=[False]*n
        self.adjacent_nodes=[[] for _ in range(n)]
        max_income=float('-inf')
        for edge in edges:
            self.adjacent_nodes[edge[0]].append(edge[1])
            self.adjacent_nodes[edge[1]].append(edge[0])
        print(self.adjacent_nodes)
        self.find_bob_path(bob,0)
        nodes_queue=deque([(0,0,0)])
        while nodes_queue:
                print(nodes_queue)
                source,time,income=nodes_queue.popleft()
                
                if ( source not in self.bob_path or time<self.bob_path[source]):
                    income+=amount[source]
                elif time==self.bob_path[source]:
                      income+=amount[source]//2 
                if len(self.adjacent_nodes[source])==1 and source!=0:
                    max_income=max(max_income,income)
                for adj in self.adjacent_nodes[source]:
                    if not self.visited_alice[adj]:
                        nodes_queue.append([adj,time+1,income])
                self.visited_alice[source]=True 
        print(max_income)
        
    def find_bob_path(self,source,time):
        print(source)
        self.bob_path[source]=time 
        self.visited_bob[source]=True 
       
        if source==0: return True 
        
        for adj in self.adjacent_nodes[source]:
            if not self.visited_bob[adj]:
                if self.find_bob_path(adj,time+1):
                    return True 
        self.bob_path.pop(source,None)
        return False 
          
        
sol=Solution()
sol.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]],3,[-2,4,2,-4,6])