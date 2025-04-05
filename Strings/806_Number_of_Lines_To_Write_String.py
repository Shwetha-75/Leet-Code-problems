class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        pixels,line=0,1 
        for i in range(len(s)):
            pixels+=widths[ord(s[i])-97]
            if pixels==100:
               line+=1 
               pixels=0 
               if i==len(s)-1:
                   pixels=100 
                   line=1 
                   
            elif pixels>100:
                line+=1 
                pixels=widths[ord(s[i])-97]
        return [line,pixels]


class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz")==[3,60]
      def testing_case_two(self):
          assert Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")==[2,4]
      def testing_case_three(self):
          assert Solution().numberOfLines([3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2],"mqblbtpvicqhbrejb")==[1,100]
          