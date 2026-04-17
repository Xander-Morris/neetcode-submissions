class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> nums_set;

        for (int num : nums) {
            if (find(nums_set.begin(), nums_set.end(), num) != nums_set.end()) { return true; }
            nums_set.insert(num);
        }

        return false;
    }
};
