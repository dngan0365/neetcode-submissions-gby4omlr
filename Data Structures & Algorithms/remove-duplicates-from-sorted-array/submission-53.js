// class Solution {
//     /**
//      * @param {number[]} nums
//      * @return {number}
//      */
//     removeDuplicates(nums) {
//         let n = nums.length;
//         let left = 0;
//         let right = 1;
//         for (right; right < n ; right++){
//             if (nums[left] != nums[right]){
//                 left++;
//                 nums[left] = nums[right];
//             }
//         }
//         return left+1;
//     }
// }

class Solution {
    removeDuplicates(nums) {
        const unique = Array.from(new Set(nums)).sort((a, b) => a -b);
        for (let i = 0; i< unique.length; i++) {
            nums[i] = unique[i];
        }
        return unique.length;
    }
}
