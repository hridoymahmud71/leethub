public class Solution {
    public int Search(int[] nums, int target) {
        
        int minIndex = 0;
        int maxIndex = nums.Length - 1;
        
        while(minIndex <= maxIndex) {
            int midIndex = minIndex +  ((maxIndex - minIndex) / 2) ;
            
            if(target == nums[midIndex]){
                return midIndex;
            } else if (target < nums[midIndex]){
                 maxIndex = midIndex - 1;
            } else {
                 minIndex  = midIndex + 1;
            }
        }
        
        return -1;
        
    }
}