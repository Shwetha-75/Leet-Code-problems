// Given an array of positive integers nums and a positive integer target, return the minimal length of a 
// subarray
//  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


// Example 1:

// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: The subarray [4,3] has the minimal length under the problem constraint.
// Example 2:

// Input: target = 4, nums = [1,4,4]
// Output: 1
// Example 3:

// Input: target = 11, nums = [1,1,1,1,1,1,1,1]
// Output: 0
 

// Constraints:

// 1 <= target <= 109
// 1 <= nums.length <= 105
// 1 <= nums[i] <= 104.


class MnimumSizeSubArraySum{
    public static void main(String[] args) {
        
    }
    public static int minSubArrayLen(int nums[],int target){
        int left=0,right=0,n=nums.length,min_len=Integer.MAX_VALUE,sum=0;

        while(right<n){
            sum+=nums[right];
            while(sum>=target){
                min_len=Math.min(min_len,right-left+1);
                sum-=nums[left];
                left+=1;
            }
            right+=1;
        }

        return min_len!=Integer.MAX_VALUE? min_len :0;
    }
}