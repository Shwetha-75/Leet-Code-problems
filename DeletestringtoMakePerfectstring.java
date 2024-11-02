import java.util.*;

class DeletestringtoMakePerfectstring{
    public static void main(String[] args) {
        
    }

    public String deleteStringMake(String input){
        List<String> list=new LinkedList();
        if(input.length()>=3)
        {
            list.add(input.charAt(0)+"");
            list.add(input.charAt(1)+"");
            for(int i=2;i<input.length();i++)
            {
                if(!(list.get(list.size()-2).equals(list.size()-1) && (list.get(list.size()-2).equals(input.charAt(i)+""))))
                {
                    list.add(input.charAt(i)+"");
                }
            }

        }
        return list.toString().replaceAll(",","");
    }
}