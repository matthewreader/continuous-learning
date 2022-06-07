struct Solution;

impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let gague = candies.iter().max().unwrap() - extra_candies;
        let v: Vec<bool> = candies.iter().map(|x| x >= &gague).collect();
        v
    }
}
