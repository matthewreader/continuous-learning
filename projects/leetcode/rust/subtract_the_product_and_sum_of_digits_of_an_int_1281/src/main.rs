struct Solution;

impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        let s = n.to_string();
        let v = s.chars().map(|x| x.to_digit(10).unwrap() as i32);
        let product: i32 = v.clone().product();
        let sum: i32 = v.sum();
        product - sum
    }
}