class MinStack {
private:
    stack<int> int_stack;

public:
    MinStack() {

    }
    
    void push(int val) {
        int_stack.push(val);
    }
    
    void pop() {
        int_stack.pop();
    }
    
    int top() {
        return int_stack.top();
    }
    
    int getMin() {
        stack<int> mock_stack = int_stack;
        int minimum = 0, iterator = 0;

        while (!mock_stack.empty()) {
            if (iterator == 0 || mock_stack.top() < minimum) {
                minimum = mock_stack.top();
            }

            mock_stack.pop();
            iterator++;
        }

        return minimum;
    }
};
