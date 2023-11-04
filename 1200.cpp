class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int min_diff = INT_MAX;
        for (int i = 0; i < arr.size() - 1; i++) {
            if (abs(arr.at(i) - arr.at(i + 1)) < min_diff) {
                min_diff = abs(arr.at(i) - arr.at(i + 1));
            }
        }

        vector<vector<int>> ans;
        for (int i = 0; i < arr.size() - 1; i++) {
            if (abs(arr.at(i) - arr.at(i + 1)) == min_diff) {
                ans.push_back({arr.at(i), arr.at(i + 1)});
            }
        }

        return ans;
    }
};

