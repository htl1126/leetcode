class Bank {
public:
    Bank(vector<long long>& bank_balance) {
        balance.assign(bank_balance.begin(), bank_balance.end());
        n = balance.size();
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (1 <= account1 && account1 <= n && 1 <= account2 && account2 <= n && balance[account1 - 1] >= money) {
            balance[account1 - 1] -= money;
            balance[account2 - 1] += money;
            return true;
        }
        return false;
    }
    
    bool deposit(int account, long long money) {
        if (1 <= account && account <= n) {
            balance[account - 1] += money;
            return true;
        }
        return false;
    }
    
    bool withdraw(int account, long long money) {
        if (1 <= account && account <= n && balance[account - 1] >= money) {
            balance[account - 1] -= money;
            return true;
        }
        return false;
    }
private:
    int n;
    vector<long long> balance;
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
