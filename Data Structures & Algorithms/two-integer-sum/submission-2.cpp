class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> value_to_index;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (value_to_index.find(complement) != value_to_index.end()) { return {value_to_index[complement], i}; }
            value_to_index[nums[i]] = i;
        }
    }
};
