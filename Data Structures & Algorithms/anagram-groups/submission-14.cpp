class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> anagrams;
        std::unordered_map<int, std::unordered_map<char, int>> map;
        std::unordered_map<int, bool> in_anagram;

        for (int i = 0; i < strs.size(); i++) {
            if (strs[i].size() == 0) { map[i]['\''] = 1; continue; }
            for (char c : strs[i]) { map[i][c]++; };
        }

        for (const auto &pair : map) {
            if (in_anagram[pair.first]) { continue; }
            std::vector<std::string> pairs;
            pairs.push_back(strs[pair.first].size() == 0 ? "" : strs[pair.first]);

            for (const auto &other_pair : map) {
                if (in_anagram[other_pair.first]) { continue; }
                if (other_pair.first == pair.first) { continue; }
                bool matched = true;
                
                if (strs[pair.first].size() >= strs[other_pair.first].size()) {
                    for (const auto &char_pair : pair.second) {
                        if (map[other_pair.first][char_pair.first] != char_pair.second) { matched = false; break; }
                    }
                } else {
                    for (const auto &char_pair : other_pair.second) {
                        if (map[pair.first][char_pair.first] != char_pair.second) { matched = false; break; }
                    }
                }

                if (!matched) { continue; }
                pairs.push_back(strs[other_pair.first].size() == 0 ? "" : strs[other_pair.first]);
                in_anagram[other_pair.first] = true;
            }

            anagrams.push_back(pairs);
            in_anagram[pair.first] = true;
        }

        return anagrams;
    }
};
