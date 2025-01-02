'''
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
 

Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 105
1 <= queries.length <= 105
0 <= li <= ri < words.length.

'''

class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        # Pre-computing prefix-sum
        # check for each word in words its starting and ending character in vowels list object
        # add the sum of such words to prefix_sum array 
        # Initialize ans array of length of queries and fill it with zero
        # append to ans for each query:
        #                   by taking difference between value range[left-1,right]
                            #  if the query[left ] is zero then take 0 (-1 index out of range) 
        n=len(words)
        result=[0]*len(words)
        sum=0
        vowel=['a','e','i','o','u']
        for i in range(n):
            if words[i][0] in vowel and words[i][-1] in vowel:
                sum+=1
            result[i]=sum   
        ans=[0]*(len(queries))
        for i in range(len(queries)):
            ans[i]=result[queries[i][1]]-(0 if queries[i][0]==0 else result[queries[i][0]-1])
        return ans
class TestApp:
    def testing_case_one(self):
        Solution().vowelStrings(["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]])==[2,3,0]
    
    def testing_case_two(self):
        Solution().vowelStrings(["a","e","i"],[[0,2],[0,1],[2,2]])==[3,2,1]
    def testing_case_three(self):
        Solution().vowelStrings(["b","rmivyakd","kddwnexxssssnvrske","vceguisunlxtldqenxiyfupvnsxdubcnaucpoi","nzwdiataxfkbikbtsjvcbjxtr","wlelgybcaakrxiutsmwnkuyanvcjczenuyaiy","eueryyiayq","bghegfwmwdoayakuzavnaucpur","ukorsxjfkdojcxgjxgmxbghno","pmgbiuzcwbsakwkyspeikpzhnyiqtqtfyephqhl","gsjdpelkbsruooeffnvjwtsidzw","ugeqzndjtogxjkmhkkczdpqzwcu","ppngtecadjsirj","rvfeoxunxaqezkrlr","adkxoxycpinlmcvmq","gfjhpxlzmokcmvhjcrbrpfakspscmju","rgmzhaj","ychktzwdhfuruhpvdjwfsqjhztshcxdey","yifrzmmyzvfk","mircixfzzobcficujgbj","d","pxcmwnqknyfkmafzbyajjildngccadudfziknos","dxmlikjoivggmyasaktllgmfhqpyznc","yqdbiiqexkemebyuitve"],[[5, 21],[17, 22],[19, 23],[13, 15],[20, 23],[21, 23],[6, 20],[1, 8],[15, 20],[17, 22],[6, 6],[1, 2],[4, 11],[14, 23],[7, 10],[16, 22],[20, 22],[21, 22],[15, 18],[5, 16],[17, 23]])==[2,0,0,0,0,0,2,1,0,0,0,0,2,0,1,0,0,0,0,2,0]
    
    