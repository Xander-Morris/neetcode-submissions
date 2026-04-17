class Solution {
public:
    bool isValid(string s) {
        stack<char> c_stack;
        unordered_map<char, char> c_to_o_map = {{')', '('}, {']', '['}, {'}', '{'}};

        char *c = &s[0];

        while (*c != '\0') {
            if (c_to_o_map[*c]) {
                if (!c_stack.empty() && c_stack.top() == c_to_o_map[*c]) {
                    c_stack.pop();
                } else {
                    return false;
                }
            } else {
                c_stack.push(*c);
            }

            c++;
        }

        return c_stack.empty();
    }
};