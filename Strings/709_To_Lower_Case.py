class Solution:
    def toLowerCase(self, s: str) -> str:
        temp=list(s)
        for i in range(len(temp)):
            if ord(temp[i])>=65 and ord(temp[i])<=90:
                temp[i]=chr(ord(temp[i])+32)
        return "".join(temp)


class TestApp:
      def testing_case_one(self):
          assert Solution().toLowerCase("Hello")=="hello"
      def testing_case_two(self):
          assert Solution().toLowerCase("here")=="here"
      def testing_case_three(self):
          assert Solution().toLowerCase("LOVELY")=="lovely"