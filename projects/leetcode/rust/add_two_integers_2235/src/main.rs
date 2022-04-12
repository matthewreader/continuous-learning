struct Solution;

impl Solution {
    pub fn sum(num1: i32, num2: i32) -> i32 {
        num1 + num2
    }
}

#[test]
fn test() {
    assert_eq!(Solution::sum(1, 2), 3);
    assert_eq!(Solution::sum(-1, 5), 4);
}