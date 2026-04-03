#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), left = 0, right = 1;
        for (right ; right < n; right++){
            if (nums[left] != nums[right]){
                left ++;
                nums[left] = nums[right];
            }
        }
        return (left + 1);
    }
};