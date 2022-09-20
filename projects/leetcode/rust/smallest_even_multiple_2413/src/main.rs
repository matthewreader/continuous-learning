struct Solution;

impl Solution {
    pub fn smallest_even_multiple(n: i32) -> i32 {
        if n % 2 != 1 {
            return n 
        }
        else {
            return n * 2
        }
    }
}

#[test]
fn test_even() {
    assert_eq!(Solution::smallest_even_multiple(6), 6);
}
#[test]
fn test_odd() {
    assert_eq!(Solution::smallest_even_multiple(5), 10);
}
