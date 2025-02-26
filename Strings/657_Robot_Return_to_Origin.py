from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
    
        map=dict(Counter(moves))
        if len(map)%2!=0: return False 
        else:
            if len(map)==2:
                if ("L" in map and "U" in map) or ("R" in map and "U" in map) or ("L" in map and "D" in map) or("R" in map and "D" in map):
                    return False 
                
                if "L" in map and "R" in map:
                    return map["L"]==map["R"]
                else:
                    return map["U"]==map["D"]
            else:
                return map["L"]==map["R"] and map["U"]==map["D"]
    
     
class TestApp:
        def testing_case_one(self):
            assert Solution().judgeCircle("UD")==True 
        
        def testing_case_two(self):
            assert Solution().judgeCircle("LL")==False 
                
        def testing_case_three(self):
            assert Solution().judgeCircle("UDDUURLRLLRRUDUDLLRLURLRLRLUUDLULRULRLDDDUDDDDLRRDDRDRLRLURRLLRUDURULULRDRDLURLUDRRLRLDDLUUULUDUUUUL")==False
            
