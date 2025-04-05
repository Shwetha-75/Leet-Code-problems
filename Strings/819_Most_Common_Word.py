from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph="".join([word.lower() if word.isalnum() else " " for word in paragraph ])
        paragraph=paragraph.split(" ")
        hash_map=defaultdict(int)
        for word in paragraph:
            if word in banned:
                continue 
            elif word:
                hash_map[word]+=1 
        hash_map=list(hash_map.items())
        hash_map.sort(reverse=True,key=lambda x:x[1])
        return hash_map[0][0]


class TestApp:
      def testing_case_one(self):
          assert Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])=="ball"
      def testing_case_two(self):
          assert Solution().mostCommonWord("a.",[])=="a"
                
        
        