import heapq
class Solution:
    def maxTwoEvents(self,events:list[list[int]]):
        # Approach failed !! :[[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]]
        # result=[]
        # events.sort(key=lambda x:x[0])
        # print(events)
        # end_time=events[0][1]
        # value=events[0][2]
        # for i in range(1,len(events)):
        #     if end_time<events[i][0]:
        #         value+=events[i][2]
        #         result.append(value)
        #         end_time=events[i][1]
        #         value=events[i][2]
        #     elif events[i-1][1]<events[i][0]:
        #         result.append(events[i-1][2]+events[i][2])
        #     else:
        #         result.append(events[i][2])
        # return max(result)
        result=[]
        events.sort(key=lambda x:x[0])
        max_sum,max_val=0,0
        for event in events:
            print(result)
            while result and result[0][0]<event[0]:
                  max_val=max(max_val,result[0][1])
                  heapq.heappop(result)
            max_sum=max(max_sum,max_val+event[2])
            heapq.heappush(result,(event[1],event[2]))
        return max_sum
        
def main():
    sol=Solution()
    result=sol.maxTwoEvents([[19,36,24],[70,90,11],[61,78,36],[38,38,70],[39,83,72],[8,46,5],[64,69,49],[88,89,39],[53,77,24],[35,76,26]])
    print(result)
main()