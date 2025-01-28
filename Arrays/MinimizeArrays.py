class Solution:
    def makingValidString(self,s:str):
        # wrong
        # starting_index=s.index("1")
        # ending_index=s.rfind("1")
        # substring_1=""
        # substring_2=""
        # n=len(s)
        # operations=0
        # substring_1=s[:ending_index+1:]
        # substring_2=s[ending_index+1::]
        # # check for the eve length 
        # if len(substring_1)%2==0 and len(substring_2)%2==0:
        #     #check the count of i's and 0's
        #     # check for 1's 
        #     count_zero=substring_1.count("0")
        #     count_one=substring_1.count("1")
        #     operations+=min(count_one,count_zero)
        #     print(operations)
        #     count_zero=substring_2.count("0")
        #     count_one=substring_2.count("1")
        #     operations+=min(count_one,count_zero)
        # elif not substring_2:
            
        #     operations+=min(substring_1.count("1"),substring_2.count("0"))
        # else:
        #     cnt_zero_1=substring_1.count("0")
        #     cnt_one_1=substring_1.count("1")
        #     if cnt_zero_1<cnt_one_1:
        #         if "1" in substring_2:
        #            substring_1+="1"
        #            substring_2=substring_2.replace("1")
        #         else:
        #             substring_1+="0"
        #             substring_2=substring_2.replace("0","")
        #     else:
        #         if "0" in substring_2:
        #            substring_1+="0"
        #            substring_2=substring_2.replace("0")
        #         else:
        #             substring_1+="1"
        #             substring_2=substring_2.replace("1","")       
            
        #     operations+=min(substring_1.count("1"),substring_1.count("0"))
        #     operations+=min(substring_2.count("1"),substring_2.count("0"))
        # return operations 
        
        count=0 
        n=len(s)
        for i in range(0,n,2):
            temp=s[i:min(i+2,n):]
            if "1" in temp and "0" in temp:
                count+=1 
        return count
        
class TestApp:
    def testing_case_one(self):
        assert Solution().makingValidString("1110011000")==3 
    def testing_case_two(self):
        assert Solution().makingValidString("100110")==3
    def testing_case_three(self):
        assert Solution().makingValidString("101011")==2
    def testing_case_four(self):
        assert Solution().makingValidString("101010")==3
    def testing_case_five(self):
        assert Solution().makingValidString("111000")==1
    def testing_case_six(self):
        assert Solution().makingValidString("100011")==1