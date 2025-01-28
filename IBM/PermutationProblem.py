'''
Problem Statement 2
You were learning the array data structure till your friend challenged you with a problem. Given an array of queries of positive integers between 1 and k, you have to process all queries[i]  according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].

For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P.

Notice that the position of queries[i] in the permutation P is the result for queries[i]. Print an array containing the result for the given queries.

Input Format
The first line contains m, the initial permutation P = [1,2,3,….,m]

The following line contains q, the number of queries

The following line contains q numbers denoting the ith query, starting from 0 to q-1.

Output Format
Print the result of all queries in a space-separated single-line fashion.

Constraints
1<=m<=5*10^4

1<=q<=m

1<=queries[i]<=m

'''

class Solution:
    def permutation(self,p:int,q:int,queries:list[int]):
        permutation=[i for i in range(1,p+1)]
        result=[]
        for i in queries:
            index=permutation.index(i)
            result.append(index)
            value=permutation.pop(index)
            permutation.insert(0,value)
        return result 

class TestApp:
    def testing_case_one(self):
        assert Solution().permutation(6,5,[5 ,1 ,3, 4,2])==[4, 1, 3, 4, 4]
        
    def testing_case_two(self):
        assert Solution().permutation(4,4,[1 ,3 ,2 ,4])==[0 ,2, 2, 3]