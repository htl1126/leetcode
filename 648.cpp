// Ref: https://leetcode.com/problems/replace-words/solutions/105855/c-trie-with-optimizations-50-ms

class trie {
    bool isLeaf = false;
    vector<trie *> children = vector<trie *>(26, nullptr);
public:
    void insert(string& w, int cur, int end) {
        isLeaf |= cur == end;
        if (!isLeaf) {  // if we have w = "ab" and another w = "abc", we only create nodes for "ab" (root of shortest length)
            if (children[w[cur] - 'a'] == nullptr) {
                children[w[cur] - 'a'] = new trie();
            }
            children[w[cur] - 'a']->insert(w, cur + 1, end);
        }
    }
    int find(string& w, int start, int len, int end) {
        if (start + len == end || w[start + len] == ' ' || this->isLeaf) {
            return len;
        }
        if (children[w[start + len] - 'a'] == nullptr) {  // arrive at a leaf node early -- not found
            while (start + len < end && w[start + len] != ' ') {
                len++;
            }
            return len;
        }
        return children[w[start + len] - 'a']->find(w, start, len + 1, end);
    }
};

