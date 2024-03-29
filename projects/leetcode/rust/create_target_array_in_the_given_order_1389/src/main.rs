struct Solution;

impl Solution {
    pub fn create_target_array(nums: Vec<i32>, index: Vec<i32>) -> Vec<i32> {
        let mut v: Vec<i32> = Vec::with_capacity(nums.len());
        for (n, i) in nums.into_iter().zip(index.into_iter()) {
            v.insert(i as usize, n);
        }
        return v;
    }
}

#[test]
fn test() {
    assert_eq!(Solution::create_target_array(vec![0,1,2,3,4], vec![0,1,2,2,1]), vec![0,4,1,3,2]);
}