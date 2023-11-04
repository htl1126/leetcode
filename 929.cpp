// Ref: https://leetcode.com/problems/unique-email-addresses/solutions/317207/c-concise-solution

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> str_set;
        for (const auto& e : emails) {
            string clean_email;

            for (const auto& c : e) {
                if (c == '+' || c == '@') {
                    break;
                } else if (c == '.') {
                    continue;
                }
                clean_email += c;
            }
            clean_email += e.substr(e.find("@"));
            str_set.insert(clean_email);
        }
       
        return str_set.size();
    }
};

