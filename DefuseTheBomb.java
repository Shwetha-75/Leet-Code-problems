import java.util.*;

class DefuseTheBomb{
    public static void main(String[] args) {
        int arr[]={2,4,9,3};
        int k=-2;
        int result[]=decrypt(arr, k);
        for (int i : result) {
            System.err.println(i);
        }
    }

    public static int[] decrypt(int code[],int k){
        List<Integer> list=new LinkedList();
        if(k==0){
            return new int[code.length];
        }
        int n=code.length*2,index=0,length=code.length;
        for(int i=0;i<n;i++){
            if(index==code.length){
                index=0;
            }
            list.add(code[index]);
            index++;
        }
        System.out.println(list.subList(0, 3));
        int array[]=new int[code.length];
        if (k>0)
        {
            
        for(int i=0;i<code.length;i++){
            array[i]=sumOfElements(list.subList(i+1, i+k+1));
        }

        }
        else{
            k=-1*k;
            for(int i=0;i<code.length;i++){
                System.out.println((i+n-k)+"-"+(i+length));
                array[i]=sumOfElements(list.subList((i+length-k), (i+length)));
                
            }
        }
        return array;
    }
    public static int  sumOfElements(List<Integer> list){
        int sum=0;
        for(int i:list){
            sum+=i;
        }
        return sum;
    }
}