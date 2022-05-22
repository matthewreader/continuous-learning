struct Solution;

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut output_list = Vec::new();
        for i in 0..n {
            output_list.push(nums[i as usize]);
            output_list.push(nums[n as usize + i as usize]);
        }
    return output_list;
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::shuffle(vec![1,2,3,4,5,6], 3),
        vec![1,4,2,5,3,6]
    );
}
