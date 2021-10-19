type Bank struct {
    balance []int64
    n int
}


func Constructor(balance []int64) Bank {
    var b Bank
    b.balance = make([]int64, len(balance))
    copy(b.balance, balance)
    b.n = len(b.balance)
    return b
}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    if 1 <= account1 && account1 <= this.n && 1 <= account2 && account2 <= this.n && this.balance[account1 - 1] >= money {
        this.balance[account1 - 1] -= money
        this.balance[account2 - 1] += money
        return true
    }
    return false
}


func (this *Bank) Deposit(account int, money int64) bool {
    if 1 <= account && account <= this.n {
        this.balance[account - 1] += money
        return true
    }
    return false
}


func (this *Bank) Withdraw(account int, money int64) bool {
    if 1 <= account && account <= this.n && this.balance[account - 1] >= money {
        this.balance[account - 1] -= money
        return true
    }
    return false
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */
