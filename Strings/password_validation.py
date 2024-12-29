# Password Validation 
# 1. At least one lower case
# 2. At least one upper case 
# 3. At least one special symbol
# 4. At least one numeric character 
# 5. Password string length as to be 8-15 character length 
import re

class Solution:
    def password_validation(self,password:str)-> bool:
        # check if the length is matching or not 
        if len(password)<8 or len(password)>15: return False
        
        return (len(re.findall("[a-z]",password))!=0 
                and len(re.findall("[A-Z]",password))!=0 
                and len(re.findall("[0-9]",password))!=0 
                and len(re.findall("[!~$#&^%]",password))!=0
            )
        
class TestApp:
    def test_case_one(self):
        assert Solution().password_validation("123asdfg")==False 
    
    def test_case_two(self):
        assert Solution().password_validation("Shwetha&123")==True
    
    def test_case_three(self):
        assert Solution().password_validation("asdfghW45678##2#")==False 
    
    def test_case_four(self):
        assert Solution().password_validation("dfghjk!Fgh12")==True
        
