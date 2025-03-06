class Solution:
      def insertionSort(self,nums:list[int])->list[int]:
            for i in range(1,len(nums)):
                temp=nums[i]
                j=i-1 
                while j>=0 and temp<nums[j]:
                    nums[j+1]=nums[j]
                    j-=1 
                print(nums)
                nums[j+1]=temp 
            return nums 
class TestApp:
        def testing_case_one(self):
            assert Solution().insertionSort([4,3,1,2,5])==[1,2,3,4,5]   
        def testing_case_two(self):
            assert Solution().insertionSort([1,2,3,4,5])==[1,2,3,4,5]
        def testing_case_three(self):
            assert Solution().insertionSort([3,3,3,2,1,1,1,0,5,5])==[0,1,1,1,2,3,3,3,5,5]
        def testing_case_four(self):
            assert Solution().insertionSort([5,4,3,1,8,9,0])==[0,1,3,4,5,8,9]