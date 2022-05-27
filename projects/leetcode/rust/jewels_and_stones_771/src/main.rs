struct Solution;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut count: i32 = 0;
        
        for c in jewels.chars() {
            count = count + stones.matches(c).count() as i32;
        }
        count
    }
}

#[test]
fn test() {
    assert_eq!(Solution::num_jewels_in_stones("aA".to_string(), "aAAbbbbbb".to_string()), 3);
}