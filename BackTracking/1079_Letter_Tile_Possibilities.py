'''
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.

Seen this question in a real interview before?
1/5
Yes
No

Accepted
133K
Submissions
169K
Acceptance Rate
78.7%

Topics
Hash Table
String
Backtracking
Counting
Companies

Hint 1
Try to build the string with a backtracking DFS by considering what you can put in every position.
Discussion (64)


'''

# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         # Calculating the subset 
#         result=[]
#         def generateSubsetByVaryingLength(string,subset:list,index:int):
#             if index==len(string):
#                 if "".join(subset) not in result and subset:
#                     result.append("".join(subset))
#                 return 
            
#             generateSubsetByVaryingLength(string,subset,index+1)
            
#             subset.append(string[index])
#             generateSubsetByVaryingLength(string,subset,index+1)
#             subset.pop()
        
#         generateSubsetByVaryingLength(tiles,[],0)
#         print(result)
#         res=result[::]
#         def permutation(string:list,i:int):
#             if i==len(string)-1:
#                 temp="".join(string)
#                 if temp not in res:
#                     res.append(temp)
#                 return
#             for j in range(i,len(string)):
#                 # swap
#                 string[i],string[j]=string[j],string[i]
#                 permutation(string,i+1)
#                 string[i],string[j]=string[j],string[i]
            
#         for i in result:
#             if len(i)>1:
#                 permutation(list(i),0)
            
#         return len(res)
from collections import Counter
class Solution:
        def numTilePossibilities(self, tiles: str) -> int:
        #   Using Depth First Search (DFS)
         
    
           return self.dfsAlgorithm(dict(Counter(tiles)))
        def dfsAlgorithm(self,hash_map):
            combo=0 
            for tile,count in hash_map.items():
                if count>0:
                    combo+=1 
                    hash_map[tile]-=1
                    combo+=self.dfsAlgorithm(hash_map)
                    hash_map[tile]+=1 
            return combo
            
class TestApp:
    def testing_case_one(self):
        assert Solution().numTilePossibilities('AAB')==8 
    
    def testing_case_two(self):
        assert Solution().numTilePossibilities('AAABBC')==188 