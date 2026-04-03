// class Solution {
//     public int[] getConcatenation(int[] nums) {
//         List<Integer> ans = new ArrayList<>();
//         for (int i = 0; i < 2*nums.length; i++) {
//             if (i < nums.length) {
//                 ans.add(nums[i]);
//             } else {
//                 ans.add(nums[i-nums.length]);
//             }
//         }
//         return ans.stream().mapToInt(Integer::intValue).toArray();
//     }
// }

public class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n * 2];
        for (int i = 0; i < n; i++) {
            ans[i] = ans[i+n] = nums[i];
        }
        return ans;
    }
}


