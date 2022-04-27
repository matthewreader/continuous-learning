struct Solution;

impl Solution {
    pub fn minimum_sum(num: i32) -> i32 {
        let mut v: Vec<char> = num.to_string().chars().collect();
        v.sort();
        let num1: String = v[0].to_string() + &v[2].to_string();
        let num2: String = v[1].to_string() + &v[3].to_string();
         return num1.parse::<i32>().unwrap() + &num2.parse::<i32>().unwrap();;
    }
}

#[test]
fn test() {
    assert_eq!(Solution::minimum_sum(1234), 37);
}

fn main() {
    println!("{}", Solution::minimum_sum(1234));
}