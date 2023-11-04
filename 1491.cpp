class Solution {
public:
    double average(vector<int>& salary) {
        int min_v = 1000001, max_v = 999;
        double sum;
        for (const auto& v : salary) {
            sum += v;
            min_v = min(min_v, v);
            max_v = max(max_v, v);
        }
        return (sum - min_v - max_v) / (salary.size() - 2);
    }
};

