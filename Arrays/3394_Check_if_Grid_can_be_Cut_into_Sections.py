class Solution:
    def checkValidCuts(self, n: int, rectangles:list[list[int]]) -> bool:
        x_points=[]
        y_points=[]
        for rectangle in rectangles:
            x_points.append([rectangle[0],rectangle[2]])
            y_points.append([rectangle[1],rectangle[3]])
        x_points.sort(key=lambda x:x[0])
        y_points.sort(key=lambda x:x[0])
        stack_x=[x_points[0]]
        stack_y=[y_points[0]]
        for i in range(1,len(x_points)):
            if stack_x[-1][1]>x_points[i][0]:
                stack_x[-1]=[stack_x[-1][0],max(stack_x[-1][1],x_points[i][1])]
            else:
                stack_x.append(x_points[i])
        for i in range(1,len(y_points)):
            if stack_y[-1][1]>y_points[i][0]:
                stack_y[-1]=[stack_y[-1][0],max(stack_y[-1][1],y_points[i][1])]
            else:
                stack_y.append(y_points[i])
        print(x_points)
        print(stack_x)
        print(stack_y)
        return len(stack_x)>2 or len(stack_y)>2
Solution().checkValidCuts(5,[[0,0,1,3],[1,0,2,2],[2,0,3,2],[1,2,3,3]])