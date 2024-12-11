public class SumOfAllLengthSubArrays {
    public static void main(String[] args) {
        
    }
    public static int sumOddLengthSubarrays(int[] array){
        int n=array.length,sum_value=0;
        for(int i=0;i<n;i++){
            int val=array[i],l=i,r=n-i-1;
            sum_value+=val*((l/2)+1)*((r/2)+1);
            sum_value+=val*((l+1)/2)*((r+1)/2);
        }
        return sum_value;
    }
}
