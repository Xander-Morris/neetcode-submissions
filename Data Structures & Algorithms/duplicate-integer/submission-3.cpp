class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        const int size = nums.size();
        if (size == 0) { return false; }
        sort(nums.begin(), nums.end());
        int i = 0;

        for (i; i < size - 1; i++) {
            if (nums[i] == nums[i + 1]) { return true; }
        }

        return false;
    }
};
