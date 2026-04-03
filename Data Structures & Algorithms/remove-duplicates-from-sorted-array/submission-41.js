class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let n = nums.length;
        let left = 0;
        let right = 1;
        for (right; right < n ; right++){
            if (nums[left] != nums[right]){
                left++;
                nums[left] = nums[right];
            }
        }
        return left+1;
    }
}
