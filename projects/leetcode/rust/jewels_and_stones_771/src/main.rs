struct Solution;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        stones.chars().filter(|&x| jewels.contains(x))
        .count() as i32
    }    
}

#[test]
fn test() {
    assert_eq!(Solution::num_jewels_in_stones("aA".to_string(), "aAAbbbbbb".to_string()), 3);
}