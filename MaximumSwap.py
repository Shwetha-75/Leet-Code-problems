class Solution:
    def findMaximumSwap(self,nums:int):
        # Approach 1
        # list_items=list(str(nums))
        # max_number=max(list_items)
        # if list_items.index(max_number)==0:
        #     return nums 
        # else:
        #     index_max_number=list_items.index(max_number)
        #     list_items[0],list_items[index_max_number]=list_items[index_max_number],list_items[0]
        #     return int(''.join(list_items))
        # index=0
        # list_items=list(str(nums))
        # for i in range(1,len(list_items)):
        #     if list_items[i-1]<list_items[i]:
        #         print(list_items[i-1])
        #         index=i-1 
        #         break
        # if index==0:
        #     temp=max(list_items[1::])
        #     temp_index=list_items.index(temp)
        #     list_items[temp_index],list_items[0]=list_items[0],list_items[temp_index]
        #     return int(''.join(list_items))
        # find the max element
        # if index==len(list_items)-2:
        #     list_items[-1],list_items[-2]=list_items[-2],list_items[-1]
        #     return int(''.join(list_items))
        # max_index=0
        # max_ele='-1'
        # for i in range(index+1,len(list_items)):
        #     if max_ele<list_items[i]:
        #         max_ele=list_items[i]
        #         max_index=i
        # print(max_index)
        # list_items[index],list_items[max_index]=list_items[max_index],list_items[index]
        # return int(''.join(list_items))
        
        index=0
        ele=-1
        list_items=list(str(nums))
        for i in range(1,len(list_items)):
            
            if list_items[i-1]<list_items[i]:
                
                ele=list_items[i-1]
                index=i-1
                break
            else:
                index=-1
        if index==-1: return nums
        if index==0:
            temp_index=list_items.index(max(list_items[1::]))
            list_items[0],list_items[temp_index]=list_items[temp_index],list_items[0]
            return int(''.join(list_items))
        print(ele)
        index_min=list_items.index(ele)
        print(index_min)
        max_ele=list_items[index+1]
        max_index=index+1
        for i in range(index+1,len(list_items)):
            if max_ele<list_items[i]:
                max_ele=list_items[i]
                max_index=i 
        list_items[index_min],list_items[max_index]=list_items[max_index],list_items[index_min]
        return int(''.join(list_items))
def main():
    sol=Solution()
    res=sol.findMaximumSwap(2736)
    print(res)
main()