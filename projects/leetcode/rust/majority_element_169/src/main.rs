use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut m: HashMap<i32, usize> = HashMap::new();
        for x in nums {
            *m.entry(x).or_default() += 1;
        }
        let max = m.into_iter()
            .max_by_key(|(_, nums)| *nums)
            .map(|(key, _)| key);
        max.unwrap()
    }
}
