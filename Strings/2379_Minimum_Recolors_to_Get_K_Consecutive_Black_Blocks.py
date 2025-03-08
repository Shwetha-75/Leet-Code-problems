import sys
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimumLength=sys.maxsize 
        n=len(blocks)
        for i in range(n-k+1):
            temp=blocks[i:i+k:].count('W')
       
            if temp==0:
                return 0 
            else:
                minimumLength=min(minimumLength,temp)
        return minimumLength 

class TestApp:
      def testing_case_one(self):
          assert Solution().minimumRecolors("WBBWWBBWBW",7)==3
      def testing_case_two(self):
          assert Solution().minimumRecolors("WBWBBBW",2)==0
        