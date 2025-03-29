from collections import Counter
class Solution: 
     
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_jewels=dict(Counter(jewels))
        hash_stones=dict(Counter(stones))
        count=0
        for key in hash_jewels:
            if key in hash_stones:
                count+=hash_stones[key]
        return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().numJewelsInStones("aA","aAAbbbb")==3 
      def testing_case_two(self):
          assert Solution().numJewelsInStones("z","ZZ")==0