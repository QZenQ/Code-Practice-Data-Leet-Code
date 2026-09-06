class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> data;
        dfs(0, 0, "", n, data);
        return data;        
    }

private:
    void dfs(int initialP, int endP, string parenthesisString, int n, vector<string>& data) {
        if (initialP == endP && initialP + endP == n * 2) {
            data.push_back(parenthesisString);
            return;
        }

        if (initialP < n) {
            dfs(initialP + 1, endP, parenthesisString + "(", n, data);
        }

        if (endP < initialP) {
            dfs(initialP, endP + 1, parenthesisString + ")", n, data);
        }
    }
};