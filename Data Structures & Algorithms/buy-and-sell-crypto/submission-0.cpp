class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0, right = 1, profit = 0;

        while (left < prices.size() && right < prices.size()) {
            if (prices[right] < prices[left]) {
                left = right;
                right = left + 1;
            } else {
                profit = std::max(profit, prices[right] - prices[left]);
                right++;
            }
        }

        return profit;
    }
};
