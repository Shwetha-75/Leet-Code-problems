class Solution:
      def licenseKeyFormatting(self, s: str, k: int) -> str:
            s=s.replace("-","")
            i=len(s)-1
            result=""
            while i>=0:
                  print(s[i:i-k:-1])
                  if i-k<0:
                      result+=s[i::-1]
                  else: result+=s[i:i-k:-1]+"-"
                  
                  i-=k 
            return result[::-1].upper() 
             
class TestApp:
      def testing_case_one(self):
          assert Solution().licenseKeyFormatting("5F3Z-2e-9-w",4)=="5F3Z-2E9W"
      def testing_case_two(self):
          assert Solution().licenseKeyFormatting("2-5g-3-J",2)=="2-5G-3J"
      def testing_case_three(self):
          assert Solution().licenseKeyFormatting("2-4A0r7-4k",4)=="24A0-R74K"


