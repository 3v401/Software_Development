#include <iostream>
#include <unordered_map>
#include <stack>

bool isValid(const std::string& s){
        std::stack<char> st;
    std::unordered_map<char, char> match = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

    for (char ch : s) {
        if (ch == '(' || ch == '{' || ch == '[') {
            st.push(ch);
        } else {
            if (st.empty() || st.top() != match[ch]) {
                return false;
            }
            st.pop();
        }
    }

    return st.empty(); 
}

int main() {
    std::string input = "({[]})";
    std::cout << (isValid(input) ? "Valid" : "Invalid") << std::endl;
    return 0;
}