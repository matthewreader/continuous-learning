struct Solution;

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        n.chars().max().unwrap() as i32 - 0x30
    }
}

#[test]
fn test() {
    assert_eq!(Solution::min_partitions("332".to_string()), 3);
}