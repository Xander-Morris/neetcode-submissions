class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> close_to_open = {{')', '('}, {']', '['}, {'}', '{'}};
        std::stack<char> char_stack;

        for (char c : s) {
            if (close_to_open.count(c) != 0) {
                if (!char_stack.empty() && char_stack.top() == close_to_open[c]) {
                    char_stack.pop();
                } else {
                    return false;
                }
            } else {
                char_stack.push(c);
            }
        }

        return char_stack.empty();
    }
};