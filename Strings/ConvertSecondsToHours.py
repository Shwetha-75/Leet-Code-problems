class Solution:
    def convertingSecondsIntoHours(self,n:int)->str:
        
        # calculate seconds 
        seconds=n%60 
        n//=60 
        minutes=n%60 
        n//=60 
        hours=n 
        return f"{hours if hours>10 else f"0{hours}" }:{minutes if minutes>10 else f"0{minutes}"}:{seconds if seconds>10 else f"0{seconds}"}"


class TestApp:
    def testing_case_one(self):
        assert Solution().convertingSecondsIntoHours(3661)=="01:01:01"
    
    def testing_case_two(self):
        assert Solution().convertingSecondsIntoHours(86399)=="23:59:59"
    
    def testing_case_three(self):
        assert Solution().convertingSecondsIntoHours(0)=="00:00:00"
    def testing_case_four(self):
        assert Solution().convertingSecondsIntoHours(43200)=="12:00:00"
    
    def testing_case_five(self):
        assert Solution().convertingSecondsIntoHours(3600)=="01:00:00"
