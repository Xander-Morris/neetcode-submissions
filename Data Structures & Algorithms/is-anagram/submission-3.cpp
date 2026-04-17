class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;
        for (char c : s) { s_map[c]++; }
        for (char c : t) { t_map[c]++; }
        if (compare_maps(s_map, t_map) == false || compare_maps(t_map, s_map) == false) { return false; }
        return true;
    }

private:
    bool compare_maps(std::unordered_map<char, int>& first_map, std::unordered_map<char, int>& second_map) {
        for (const auto& pair : first_map) {
            if (second_map[pair.first] != pair.second) { return false; }
        }

        return true;
    }
};
