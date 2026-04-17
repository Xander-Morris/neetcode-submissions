class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> result(nums.size());
        
        for (int i = 0; i < nums.size(); i++) {
            int product = 0;
            bool set = false;
            for (int left = 0; left < i; left++) {
                if (!set) {
                    set = true;
                    product = nums[left];
                    continue;
                } else {
                    product *= nums[left];
                }
            }
            for (int right = nums.size() - 1; right > i; right--) {
                if (!set) {
                    set = true;
                    product = nums[right];
                    continue;
                } else {
                    product *= nums[right];
                }
            }
            result[i] = product;
        }

        return result;
    }
};
