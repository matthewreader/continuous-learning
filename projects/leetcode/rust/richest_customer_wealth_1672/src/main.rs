use std::cmp;

struct Solution;

impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut max_account = 0;

        for account in accounts.iter() {
            let current_account = account.iter().sum();
            max_account = cmp::max(max_account, current_account);
        }

        return max_account;
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::maximum_wealth(vec![vec![1, 2, 3], vec![1, 12, 3], vec![1, 1, 1]]),
        16
    );
}
