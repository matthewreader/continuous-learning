struct Solution;

impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        nums.iter()
            .map(|i| nums.iter().filter(|j| j < &i).count() as i32)
            .collect()
    }
}

#[test]
fn test() {
    assert_eq!(Solution::smaller_numbers_than_current(vec![8,1,2,2,3]), vec![4,0,1,1,3]);
}