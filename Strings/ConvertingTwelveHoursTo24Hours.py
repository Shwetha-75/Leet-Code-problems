class Solution:
    def timeConversion(self,s:str):
        #check for AM 
        if "AM" in s:
            s=s.replace("AM","")
            hrs=int(s[:2:])
            if hrs==12:
                return f"00{s[2::]}"
            return s
          
        else:
            # convert it into military  timings
            s=s.replace("PM","")
            hrs=int(s[:2:])
            if hrs==12:
                return s 
            # add 12 to the hrs 
            hrs+=12 
            return f"{hrs}{s[2::]}"


class TestApp:
    def testing_case_one(self):
        assert Solution().timeConversion("07:05:45PM")=="19:05:45"
    
    def testing_case_two(self):
        assert Solution().timeConversion("12:00:00AM")=="00:00:00"
    def testing_case_three(self):
        assert Solution().timeConversion("12:00:00PM")=="12:00:00"
    def testing_case_four(self):
        assert Solution().timeConversion("01:00:00AM")=="01:00:00" 
    def testing_case_five(self):
        assert Solution().timeConversion("02:34:56AM")=="02:34:56"
                