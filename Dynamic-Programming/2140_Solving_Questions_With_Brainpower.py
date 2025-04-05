class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        
        n=len(questions)
        result=[0]*n
        for i in range(len(questions)):
            points=questions[i][0]
            if (i+2)+1<len(questions):
                points+=questions[i+2+1][0]
            result[i]=points 
        return max(result)


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        max_value=0 
    
        for i in range(len(questions)):
            points=questions[i][0]
            if i==0:
                temp=questions[i][1]+1
            temp=i+questions[i][1]+1 
            while temp<len(questions):
                points+=questions[temp][0]
                temp+=questions[temp][1]
            max_value=max(max_value,points)
        return max_value
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n=len(questions)
        dp=[0]*n 
        dp[n-1]=questions[n-1][0]
        
        for i in range(n-2,-1,-1):
            points=questions[i][0]
            next_index=questions[i][1]
            available_index=min(i+next_index+1,n)
            solved_points=points+(dp[available_index] if available_index<n else 0)
            skipped=dp[i+1]
            dp[i]=max(solved_points,skipped)
        return dp[0]
class TestApp:
    def testing_case_one(self):
        assert Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]])==5 
    def testing_case_two(self):
        assert Solution().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]])==7 
    def testing_case_three(self):
        assert Solution().mostPoints([[12,46],[78,19],[63,15],[79,62],[13,10]])==79
    def testing_case_four(self):
        assert Solution().mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])==157