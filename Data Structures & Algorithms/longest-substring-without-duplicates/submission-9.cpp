class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) { return 0; }
        
        int length = 1;

        for (int i = 0; i < s.size() - 1; i++) {
            std::unordered_set<char> chars;

            chars.insert(s[i]);

            for (int j = i + 1; j < s.size(); j++) {
                if (chars.find(s[j]) != chars.end()) {
                    int curr = chars.size();
                    length = std::max(length, curr);
                    break;
                 } else {
                    chars.insert(s[j]);
                }
            }

            if (chars.size() > length) {
                length = chars.size();
            }

            if (length >= s.size() - i) { break; }
        }

        return length;
    }
};
