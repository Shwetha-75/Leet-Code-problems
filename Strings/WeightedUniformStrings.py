class Solution:
    def makingWeightedUniformStrings(self,s:str,queries:list):
        # h_map=dict()
        # for i in s:
        #     if i not in h_map:
        #         h_map[i]=[ord(i),1]
        #     else:
        #         value=h_map[i][1]
        #         h_map[i][1]+=1 
        #         h_map[''.join([i]*(value+1))]=[ord(i)*(value+1),1]
        # list_value=[]
        # for i in h_map:
        #     list_value.append(h_map[i][0])
        # n=queries
        # for i in range(n):
        #     if i in list_value:
        #         queries[i]="Yes"
        #     else:
        #         queries[i]="No"
        # return queries
        # using stack 
        stack=[]
        set_value=set()
        weight=0
        for i in s:
            if stack and stack[-1]!=i:
                stack.clear()
                weight=0
            weight=ord(i)-97+1
            stack.append(i)
            set_value.add(weight)
        n=len(queries)
        for i in range(n):
            if queries[i] in set_value:
                queries[i]="Yes"
            else:
                queries[i]='No'
        return queries 
    
                
