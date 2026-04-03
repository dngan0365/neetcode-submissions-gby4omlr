class MyStack {
public:
    vector<int> nums;

    MyStack() {
        nums = vector<int>();
    }
    
    void push(int x) {
        this->nums.push_back(x);
    }
    
    int pop() {
        int val = nums.back();  
        nums.pop_back();        
        return val;
    }
    
    int top() {
        return this->nums.back();
    }
    
    bool empty() {
        if (this->nums.size() == 0){
            return true;
        }
        return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */