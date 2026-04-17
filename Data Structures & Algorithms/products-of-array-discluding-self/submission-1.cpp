class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int size = nums.size();
        vector<int> new_nums(size, 1);
        int left = 1, right = 1, i = 0;

        for (i; i < size; i++) {
            new_nums[i] *= left;
            left *= nums[i];
        }

        for (i = size - 1; i >= 0; i--) {
            new_nums[i] *= right;
            right *= nums[i];
        }

        return new_nums;
    }
};
