class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> s1_mp;

        for (char c : s1) { s1_mp[c]++; }
        for (int i = 0; i < (s2.size() - s1.size()) + 1; i++) {
            std::cout << s2[i];
            if (s1_mp.find(s2[i]) == s1_mp.end()) { continue; }
            std::unordered_map<char, int> copy = s1_mp;
            copy[s2[i]]--;
            for (int j = i + 1; j < i + s1.size(); j++) {
                if (copy.find(s2[j]) == copy.end()) { break; }
                copy[s2[j]]--;
            }
            bool valid = true;
            for (const auto &pair : copy) {
                if (pair.second != 0) { valid = false; break; }
            }
            if (valid) { return true; }
        }

        return false;
    }
};
