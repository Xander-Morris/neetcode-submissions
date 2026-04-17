class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> anagrams;
        std::unordered_map<int, std::string> map;
        std::unordered_map<int, bool> in_anagram;

        for (int i = 0; i < strs.size(); i++) {
            if (strs[i].size() == 0) { map[i] = '\''; continue; }
            std::string sorted = strs[i];
            std::sort(sorted.begin(), sorted.end());
            map[i] = sorted;
        }

        for (const auto &pair : map) {
            if (in_anagram[pair.first]) { continue; }
            std::vector<std::string> pairs;
            pairs.push_back(strs[pair.first].size() == 0 ? "" : strs[pair.first]);

            for (const auto &other_pair : map) {
                if (in_anagram[other_pair.first] || other_pair.first == pair.first || other_pair.second != pair.second) { continue; }
                pairs.push_back(strs[other_pair.first].size() == 0 ? "" : strs[other_pair.first]);
                in_anagram[other_pair.first] = true;
            }

            anagrams.push_back(pairs);
            in_anagram[pair.first] = true;
        }

        return anagrams;
    }
};
