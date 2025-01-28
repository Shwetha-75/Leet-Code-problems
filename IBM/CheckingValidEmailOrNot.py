import re

class Solution:
    def checkTheEmailIsValidOrNot(self,email:str)->bool:
        if "@" in email:
            string=email.split("@")
            # checking for domain 
            if string[1]!="hackerrank.com": return False 
            # for the string pattern 
            # check for pattern based on underscore 
            if "_" in string[0]:
                # split the string based on underscore 
                result=string[0].split("_")
                # check if the length is exceeding more than 6 
                if len(result[0])>6: return False 
                # if it containers numerics 
                if re.findall("[0-9]",result[0]):
                    return False 
                # after underscore 
                if len(result[1])>4: return False 
                # if it contains alphabets 
                if re.findall("[a-z]",result[1]): return False 
            else:
                # if it is exceeding the length 
                if len(string[0])>6: return False 
                # if it is contains
                if re.findall("[0-9]",string[0]): return False 
            return True 
        else:
            return False 
        
class TestApp:
    def testing_case_one(self):
          assert Solution().checkTheEmailIsValidOrNot("julia@hackerrank.com")==True 
    def testing_case_two(self):
          assert Solution().checkTheEmailIsValidOrNot("julia@hackerrank.com")==True 
    def testing_case_three(self):
          assert Solution().checkTheEmailIsValidOrNot("julia0_@hackerrank.com")==False 
    def testing_case_four(self):
          assert Solution().checkTheEmailIsValidOrNot("julia@gmail.com")==False 
    def testing_case_five(self):
        assert Solution().checkTheEmailIsValidOrNot("julia_0@hackerrank.com")==True 