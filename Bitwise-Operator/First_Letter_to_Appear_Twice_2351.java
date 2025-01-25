import java.util.HashSet;
import java.util.LinkedHashSet;

class First_Letter_to_Appear_Twice_2351{
    public static void main(String[] args) {
        
    }
    public char repeatedCharacter(String s) {
        
        
        HashSet<Character> set=new LinkedHashSet<>();

        for(char i :s.toCharArray()){
           if(set.contains(i)){
            return i;
           }
           set.add(i);
        }

        return '\0';
    }
}