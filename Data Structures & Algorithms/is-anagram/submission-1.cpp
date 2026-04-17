class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for (char c : s) { s_map[c]++; }
        for (char c : t) { t_map[c]++; }

        if (s.size() >= t.size()) {
            for (const auto &pair : s_map) {
                if (t_map[pair.first] != pair.second) { return false; }
            }
        } else {
            for (const auto &pair : t_map) {
                if (s_map[pair.first] != pair.second) { return false; }
            }
        }

        return true;
    }
};
