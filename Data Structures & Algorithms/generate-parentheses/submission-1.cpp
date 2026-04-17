class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::string chars;
        std::vector<std::string> result;

        backtrack(chars, result, n, 0, 0);

        return result;
    }

private:
    void backtrack(std::string &chars, std::vector<std::string> &result, int n, int open, int closed) {
        if (open == closed && open == n) {
            result.push_back(chars);
            return;
        }

        if (open < n) {
            chars += '(';
            backtrack(chars, result, n, open + 1, closed);
            chars.pop_back();
        }

        if (closed < open) {
            chars += ')';
            backtrack(chars, result, n, open, closed + 1);
            chars.pop_back();
        }
    }
};
