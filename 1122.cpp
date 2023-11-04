// Ref: https://leetcode.com/problems/relative-sort-array/solutions/364612/c-map-solution

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> m;

        for (auto const& n : arr1) {
            m[n]++;
        }
        int i = 0;
        for (auto const& n : arr2) {
            while (m[n] > 0) {
                arr1[i] = n;
                m[n]--;
                i++;
            }
        }
        for (auto const& it : m) {
            while (m[it.first] > 0) {
                arr1[i] = it.first;
                m[it.first]--;
                i++;
            }
        }

        return arr1;
    }
};

