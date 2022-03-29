impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        if low % 2 == 0 && high % 2 == 0 {
            return (high - low) / 2;
        } else {
            return ((high - low) / 2) + 1;
        }
    }
}

//fn main() {
//    println!("{}", count_odds(1, 1055));
//}