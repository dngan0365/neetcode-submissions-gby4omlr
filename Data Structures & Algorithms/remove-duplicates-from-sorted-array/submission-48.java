// class Solution {
//     public int removeDuplicates(int[] nums) {
//         int n = nums.length;
//         int left = 0;
//         int right = 1;
//         while (right < n){
//             if (nums[left] != nums[right]) {
//                 nums[left + 1] = nums[right];
//                 left++;
//             }
//             right++;
//         }
//         return left + 1;
//     }
// }

class Solution {
    public int removeDuplicates(int[] nums) {
        TreeSet<Integer> unique = new TreeSet<>();
        for (int num : nums) {
            unique.add(num);
        }
        int i = 0;
        for (int num: unique) {
            nums[i++] = num;
        }
        return unique.size();
    }
}