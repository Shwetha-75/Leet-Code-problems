from collections import Counter
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        hash_map={}
        n=len(recipes)
        for i in range(n):
            hash_map[recipes[i]]=ingredients[i]
        supplies_map=Counter(supplies)
        result_dish={}
        not_prepared={}
        for key ,values in hash_map.items():
            count=0
          
            for value in values:
                if value in supplies_map or value in result_dish:
                    count+=1 
            if count==len(values):
                result_dish[key]=1
            else:
            
                not_prepared[key]=values 
        for key,values in not_prepared.items():
            count=0 
            for value in values:
                if value in supplies_map or value in result_dish:
                    count+=1 
            if count==len(values):
                result_dish[key]=1
        
        return list(result_dish.keys())
        
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        hash_map={}
        n=len(recipes)
        for i in range(n):
            hash_map[recipes[i]]=ingredients[i]
        supplies_map=Counter(supplies)
        ingredients_map={}
        for i in ingredients:
            for each in i:
                ingredients_map[each]=1 
        result=[]
        for key,values in hash_map.items():
            count=0 
            for value in values:
                if value in supplies_map:
                    count+=1 
            if count==len(values):
                result.append(key)
                supplies_map[key]=1
     
        return result

class TestApp:
        def testing_case_one(self):
            assert Solution().findAllRecipes(["bread","sandwich"],[["yeast","flour"],["bread","meat"]],["yeast","flour","meat"])==["bread","sandwich"]
        def testing_case_two(self):
            assert Solution().findAllRecipes(["bread"],[["yeast","flour"]],["yeast","flour","corn"])==["bread"]
        def testing_case_three(self):
            assert Solution().findAllRecipes(["bread","sandwich","burger"],[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],["yeast","flour","meat"])==["bread","sandwich","burger"]
        def testing_case_four(self):
            assert Solution().findAllRecipes(["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"],
                                             [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]],
                                             
                                             ["wi","otr","wbjr","fzr","xgp"]
                                             )==["xevvq","izcad","bxgnm","i","hjvu","tokfq","z","g","b","hthy"]    
     