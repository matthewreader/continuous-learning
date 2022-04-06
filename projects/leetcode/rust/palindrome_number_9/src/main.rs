impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        
        let mut reverse: i32 = 0;
        let mut y: i32 = x;
        let r = 10;

        if y < 0 {
            return false
        };
        
        while y != 0 {
            reverse = reverse * r + y % r;
            y /= r;
        };
        
        if reverse == x {
            return true;
        } else {
            return false;
        };
    }
}

fn main() {
    let b = Solution::is_palindrome(1001);
    println!("{}", b);
}
