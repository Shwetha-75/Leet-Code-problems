import java.util.*;
class StringCompression{
    public static void main(String[] args) {
        String input="aaaaaaaaaaaaaabb";
        System.out.println(new StringCompression().compressedString(input));
    }

    public String compressedString(String word)
    {
        List<String> list=new LinkedList();
        int index=1;
        String result="";
        list.add(word.charAt(0)+"");
        while(index<word.length())
        {
            if(list.size()==9 || ! list.contains(word.charAt(index)+"")){
                result+=list.size()+""+list.get(0);
                list.clear();
            }
            list.add(word.charAt(index)+"");
            index+=1;
        }
        if( list.size()!=0){
            result+=list.size()+""+list.get(0);
        }
        return result;
    }
}