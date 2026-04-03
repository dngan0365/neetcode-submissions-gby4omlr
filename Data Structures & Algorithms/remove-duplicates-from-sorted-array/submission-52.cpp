#include <iostream>
#include <vector>
using namespace std;

// class Solution {
// public:
//     int removeDuplicates(vector<int>& nums) {
//         int n = nums.size(), left = 0, right = 1;
//         for (right ; right < n; right++){
//             if (nums[left] != nums[right]){
//                 left ++;
//                 nums[left] = nums[right];
//             }
//         }
//         return (left + 1);
//     }
// };

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> unique(nums.begin(), nums.end());
        int i = 0;
        for (int num : unique) {
            nums[i++] = num;
        }
        return unique.size();
    }
};