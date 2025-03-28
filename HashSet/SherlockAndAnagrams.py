class Solution:
      def findCountOfAnagramsSubString(self,s:str)->int: 
            count=0 
            hash_map={}
            for i in range(len(s)):
                temp=""
                for j in range(i,len(s)):
                    temp="".join(sorted(s[j]+temp))
                    if temp in hash_map:
                        hash_map[temp]+=1 
                    else:
                        hash_map[temp]=1 
            
            for key,value in hash_map.items():
                count+=(value*(value-1))//2 
            return count 
class TestApp:
        def testing_case_one(self):
            assert Solution().findCountOfAnagramsSubString("abba")==4 
        def testng_case_two(self):
            assert Solution().findCountOfAnagramsSubString("kkkk")==10 
        def testing_case_three(self):
            assert Solution().findCountOfAnagramsSubString("abcd")==0 
        def testing_case_four(self):
            assert Solution().findCountOfAnagramsSubString("ifailuhkqq")==3