// Ref: https://leetcode.com/problems/long-pressed-name/solutions/183994/c-java-python-two-pointers

class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i = 0, name_len = name.size(), typed_len = typed.size();
        for (int j = 0; j < typed_len; j++) {
            if (i < name_len && name[i] == typed[j]) {
                i++;
            } else if (!j || typed[j] != typed[j - 1]) {
                // !j deals with case name[0] != typed[0]
                return false;
            }
        }
        return i == name_len;  // make sure all the chars of name are checked
    }
};

