impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut v: Vec<i32> = Vec::new();

        for (pos, e) in nums.iter().enumerate() {
            v.push(nums[*e as usize]);
        }
    return v
    }
}
