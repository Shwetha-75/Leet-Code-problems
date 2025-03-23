# Wrong Approach 
class Solution:
    
      def findingTheMinimumSwaps(self,nums:list[int])->int:
          result=[-1]*(len(nums))
          for i in range(len(result)):
              if nums[i]==i+1:
                 result[i]=i+1 
          count=0 
          for i in result:
              if i==-1:
                  count+=1 
          return count-1 if count>0 else 0
# Wrong Approach    #  
class Solution:
      def findingTheMinimumSwaps(self,nums:list[int])->int:
            hash_map={}
            for i in range(len(nums)):
                if nums[i]!=i+1:
                    hash_map[i+1]=nums[i]
        #     Pseudo code
        #   traverse in hash_map 
        #    for present key take the value and check in hash_map if the key and value as key your finding value are matching increment the count and replace the found key value by -1 
        #    else not matching ensure that value is not -1 if not increment by 1 if it is -1 ignore it 
            for i in range(len(nums)):
                if nums[i]!=i+1:
                   index=hash_map[i+1] 
                   nums[index]=nums[i]
                   nums[i]=i+1
                   hash_map[index]=i
                   hash_map[i+1]=index
                   count+=1
            return count
Solution().findingTheMinimumSwaps([2 ,31 ,1 ,38, 29 ,5 ,44 ,6, 12 ,18 ,39 ,9 ,48 ,49 ,13 ,11, 7 ,27 ,14 ,33 ,50 ,21 ,46 ,23 ,15 ,26 ,8 ,47 ,40 ,3 ,32 ,22 ,34 ,42 ,16 ,41 ,24 ,10, 4 ,28 ,36 ,30 ,37 ,35 ,20 ,17 ,45 ,43 ,25 ,19])

# class Solution():
#       def findingTheMinimumSwaps(self,nums:list[int])->int:
#           hash_map={}
#           for i in range(len(nums)):
#               hash_map[nums[i]]=i 
#           count=0
#           for i in range(len(nums)):
#               if i+1!=nums[i]:
#                  target=i+1 
#                  curIndex=hash_map[target]
#                  hash_map[nums[i]]=curIndex 
#                  hash_map[target]=i 
#                  nums[curIndex]=nums[i]
#                  nums[i]=target 
#                  count+=1
#           return count
              
class TestApp:
    def testing_case_one(self):
        assert Solution().findingTheMinimumSwaps([4,3,1,2])==3 
    def testing_case_two(self):
        assert Solution().findingTheMinimumSwaps([2,3,4,1,5])==3
    def testing_case_three(self):
        assert Solution().findingTheMinimumSwaps([1,3,5,2,4,6,7])==3 
    def test_case_four(self):
        assert Solution().findingTheMinimumSwaps([1,2,3,4,5])==0 
    def testing_case_five(Self):
        assert Solution().findingTheMinimumSwaps([1,3,2,5,4])==2 
    def testing_case_six(self):
        assert Solution().findingTheMinimumSwaps([1,2,3,4,5,8,6,7])==2
    def testing_case_seven(self):
        assert Solution().findingTheMinimumSwaps([3,1,2,5,4])==3
    def testing_case_eight(self):
        pass         