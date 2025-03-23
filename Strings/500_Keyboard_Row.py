class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row_1={'q':0,'w':1,'e':2,'r':3,'t':4,'y':5,'u':6,'i':7,'o':8,'p':9}
        row_2={'a':0,'s':1,'d':2,'f':3,'g':4,'h':5,'j':6,'k':7,'l':8}
       
        result=[]
    
        temp=[i.lower() for i in words]
        for i in range(len(temp)):
            status=''
            flag=True 
            for j in range(len(temp[i])):
                if j==0:
                    if temp[i][j] in row_1:
                        status='row_1'
                    elif temp[i][j] in row_2:
                        status='row_2'
                    else:
                        status='row_3'
                else:
                    if temp[i][j] in row_1:
                        if status!='row_1':
                            flag=False 
                            break 
                    elif temp[i][j] in row_2:
                        if status!='row_2':
                            flag=False 
                            break 
                    else:
                        if status!='row_3':
                            flag=False 
                            break 
            if flag: 
                result.append(i)
        result=[words[i] for i in result]
        return result
Solution().findWords(["omk"])