'''

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.

'''
class Solution:
    def maxUniqueSplit(Self,s:str):
        # final_result=[]
        # temp=''
        # for i in range(len(s)):
        #     temp+=s[i]
        #     if temp not in final_result:
        #         final_result.append(temp)
        #         temp=''
        #     elif i==len(s)-1:
        #          final_result[-1]+=s[i]
                 
        #     else:
        #         #print(s[i],i)
        #         print(temp)
                
        # print(final_result)
        # return len(final_result)
        data=set()
        def helper(s:str,start:int,data:set):
            if start==len(s):
                 return 0
            max_count=0
            for end in range(start+1,len(s)+1):
                sub_string=s[start:end:]
                if sub_string not in data:
                    data.add(sub_string)
                    max_count=max(max_count,1+helper(s,end,data))
                    data.remove(sub_string)
            return max_count
        return helper(s,0,data)
def main():
    sol=Solution()
    res=sol.maxUniqueSplit("wwwzfvedwfvhsww")
    print(res)
main()