class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels={'a':1,'i':1,"o":1,"e":1,"u":1,"A":1,"I":1,"O":1,"E":1,"U":1}
        sentence=sentence.split(" ")
        count=1
        for i in range(len(sentence)):
            temp=""    
            word=sentence[i] 
            if word[0] in vowels:
                word+="ma" 
            else:
                
                word=list(word)
                word="".join(word[1::]+[word[0]]+["ma"])  
            for _ in range(count):
                temp+="a"
            count+=1
            sentence[i]=word+temp 
        print(sentence)
        return " ".join(sentence)
Solution().toGoatLatin("I speak Goat Latin")