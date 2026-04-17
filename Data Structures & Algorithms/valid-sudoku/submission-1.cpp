class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::cout << "Row: \n";
        for (int row = 0; row < board.size(); row++) {
            std::unordered_map<char, int> frequency;
            for (int i = 0; i < board.size(); i++) {
                std::cout << board[row][i] << " ";
                if (board[row][i] < '0' || board[row][i] > '9') { continue; }
                if (frequency[board[row][i]] >= 1) { return false; }
                frequency[board[row][i]]++;
            }
            std::cout << "\n";
        }
        std::cout << "\n\n\n";

        std::cout << "Column: \n";
        for (int column = 0; column < board.size(); column++) {
            std::unordered_map<char, int> frequency;
            for (int i = 0; i < board.size(); i++) {
                std::cout << board[i][column] << " ";
                if (board[i][column] < '0' || board[i][column] > '9') { continue; }
                if (frequency[board[i][column]] >= 1) { return false; }
                frequency[board[i][column]]++;
            }
            std::cout << "\n";
        }
        std::cout << "\n\n\n";

        std::cout << "Sub-boxes: \n";
        for (int outer_sub = 0; outer_sub < board.size() / 3; outer_sub++) {
            for (int sub_box = 0; sub_box < board.size() / 3; sub_box++) {
                std::cout << "Current sub: " << sub_box << "\n";
                std::unordered_map<char, int> frequency;
                for (int row = 0; row < board.size() / 3; row++) {
                    for (int column = 0; column < board.size() / 3; column++) {
                        //std::cout << (sub_box * 3) + row << ", " << (outer_sub * 3) + column << "\n";
                        std::cout << board[(sub_box * 3) + row][(outer_sub * 3) + column] << " ";
                        if (board[(sub_box * 3) + row][(outer_sub * 3) + column] < '0' || board[(sub_box * 3) + row][(outer_sub * 3) + column] > '9') { continue; }
                        if (frequency[board[(sub_box * 3) + row][(outer_sub * 3) + column]] >= 1) { return false; }
                        frequency[board[(sub_box * 3) + row][(outer_sub * 3) + column]]++;
                    }
                    std::cout << "\n";
                }
                std::cout << "\n\n\n";
            }
        }

        return true;
    }
};
