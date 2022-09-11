use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let unique: HashSet<i32> = nums.iter().cloned().collect();
        return nums.len() > unique.len();
    }
}

#[test]
fn test_contains_dups() {
    assert_eq!(
        Solution::contains_duplicate(vec![1,2,3,4,5,6,1]),
        true
    );
}

#[test]
fn test_no_dups() {
    assert_eq!(
        Solution::contains_duplicate(vec![1,2,3,4,5,6]),
        false
    );
}


