from collections import Counter
class Solution:
      def makeStringAnagrams(self,a:str,b:str):
            hash_map_1=dict(Counter(a))
            hash_map_2=dict(Counter(b))
            count=0 
            for character in a:
                if character not in hash_map_2:
                    count+=1 
            for character in b:
                if character not in hash_map_1:
                    count+=1 
            return count
class TestApp:
      def testing_case_one(self):
          assert Solution().makeStringAnagrams("abc","cde")==4
      def testing_case_two(self):
          assert Solution().makeStringAnagrams('cde',"def")==2