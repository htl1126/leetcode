// Ref: https://leetcode.com/problems/map-sum-pairs/solutions/1371761/c-java-python-trie-hashmap-efficient-clean-concise

struct TrieNode {
    vector<TrieNode *> child = vector<TrieNode *>(26, nullptr);
    int sum = 0;
};

class MapSum {
public:
    unordered_map<string, int> map;
    TrieNode root;
   
    void insert(const string& key, int val) {
        int diff = val - map[key];
        TrieNode *cur = &root;
        for (char c : key) {
            c -= 'a';
            if (cur->child[c] == nullptr) {
                cur->child[c] = new TrieNode();
            }
            cur = cur->child[c];
            cur->sum += diff;
        }
        map[key] = val;
    }
   
    int sum(const string& prefix) {
        TrieNode *cur = &root;
        for (char c : prefix) {
            c -= 'a';
            if (cur->child[c] == nullptr) {
                return 0;
            }
            cur = cur->child[c];
        }
        return cur->sum;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */

