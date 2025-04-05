class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hash_map_strings={
            
        }
        for i in range(len(arr)):
            hash_map_strings[chr(i+97)]=arr[i]
        
        count=0 
        result_map={}
        for word in words:
            temp=""
            for char in word:
                temp+=hash_map_strings[char]
            if temp in result_map:
                result_map[temp]+=1 
            else:
                result_map[temp]=1 
        return len(result_map.keys())

class TestApp:
      def testing_case_one(self):
          assert Solution().uniqueMorseRepresentations(["gin","zen","gig","msg"])==2
      def testing_case_two(self):
          assert Solution().uniqueMorseRepresentations(["a"])==1

          