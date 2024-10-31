class Solution:
    def extraCharactersString(self,string:str,dict:list):
        result=[]
        for i in dict:
            result=string.split(i)
            string=''.join(result)
        print(result)
        return len(''.join(result))
def main():
    sol=Solution()
    result=sol.extraCharactersString("sayhelloworld",["hello","world"])
    print(result)
main()
            

