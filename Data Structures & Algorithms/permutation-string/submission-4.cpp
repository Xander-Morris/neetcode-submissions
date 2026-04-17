class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        const int s1_size = s1.size(), s2_size = s2.size();
        if (s1_size > s2_size) { return false; }
        
        std::unordered_map<char, int> s1_chars;
        int sum_of_chars = 0, i = 0, j = 0;
        bool all_chars_equal = true;

        for (char c : s1) { s1_chars[c]++; }
        for (i; i < s2_size; i++) {
            std::unordered_map<char, int> s2_chars;
            s2_chars[s2[i]]++;
            for (j = i + 1; j < std::min(i + s1_size, s2_size); j++) { s2_chars[s2[j]]++; }
            
            all_chars_equal = true;
            for (const auto& pair : s1_chars) {
                if (pair.second != s2_chars[pair.first]) {
                    all_chars_equal = false;
                    break;
                }
            }

            if (all_chars_equal) { return true; }
        }

        return false;
    }
};
