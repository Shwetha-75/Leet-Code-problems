class Solution:
    def canYouMakeDifference(n: int, s: str) -> int:
        result=set(s)
        return 1 if len(result)>1 else 0 
    
class TestApp:
      def testing_case_one(self):
          assert Solution().canYouMakeDifference("aaaa")==0 
       
      def testing_case_two(self):
          assert Solution().canYouMakeDifference("abcd")==1