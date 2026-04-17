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
public:
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> result;
        std::queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* right_side = nullptr;
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node) {
                    right_side = node;
                    q.push(node->left);
                    q.push(node->right);
                }
            }
            if (right_side) { result.push_back(right_side->val); }
        }

        return result;
    }
};
