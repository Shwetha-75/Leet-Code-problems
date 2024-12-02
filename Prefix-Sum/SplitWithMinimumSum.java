import java.util.*;

public class SplitWithMinimumSum {
    public static void main(String[] args) {
        
    }

    public static int splitNum(int num){
        List<Integer> list =new LinkedList<>();
        while(num!=0){
            int rem=num%10;
            list.add(rem);
            num/=10;
        }

        Collections.sort(list);
        int num1,num2;
        for(int i=0;i<list.size();i++){
            if(i%2==0){
                num1=num1*10+list.get(i);
            }
            else
            {
                num2=num2*10+list.get(i);
            }
        }
        return num1+num2;
    }
}
