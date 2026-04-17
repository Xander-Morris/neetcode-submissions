/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    vector<vector<int>> levels;

    void dfs(TreeNode* node, int depth) {
        if (node == NULL) { return; }

        if (levels.size() == depth) {
            levels.push_back(vector<int>());
        }

        levels[depth].push_back(node->val);
        dfs(node->left, depth + 1);
        dfs(node->right, depth + 1);
    }

public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) { return {}; }

        dfs(root, 0);

        return levels;
    }
};
