class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> result;
        std::unordered_map<int, int> mp; 
        std::priority_queue<std::pair<int, int>> q;

        for (int num : nums) { mp[num]++; }
        for (const auto &pair : mp) { q.push({pair.second, pair.first}); }
        while (result.size() < k) {
            result.emplace_back(q.top().second);
            q.pop();
        }

        return result;
    }
};
