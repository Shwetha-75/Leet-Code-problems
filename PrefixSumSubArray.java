import java.util.HashMap;
import java.util.LinkedHashMap;

public class PrefixSumSubArray{
    public static void main(String[] args) {
        int array[]={1,1,1};
        int k=2;
        System.out.println(new PrefixSumSubArray().countSubArray(array, k));
    }

    public int countSubArray(int array[],int k){
       
        int count=0,prefixSum=0;
        HashMap<Integer,Integer> hash_map=new LinkedHashMap<>();
        hash_map.put(0, 1);
 
        for(int i:array){
         prefixSum+=i;
         if(hash_map.containsKey(prefixSum-k)){
             count+=hash_map.get(prefixSum-k);
         }
         hash_map.put(prefixSum, hash_map.getOrDefault(prefixSum,0)+1);
        }
       return count;
   }
}