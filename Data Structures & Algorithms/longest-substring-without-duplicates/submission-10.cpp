class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int size = s.size();
        std::unordered_set<char> chars;
        int right = 0, left = 0, longest_sub = 0;

        for (right; right < size; right++) {
            while (chars.find(s[right]) != chars.end()) {
                chars.erase(s[left]);
                left++;
            }

            chars.insert(s[right]);
            longest_sub = std::max(longest_sub, right - left + 1);
        }

        return longest_sub;
    }
};
