impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut my_iter = s.chars().peekable();
        let mut total = 0;

        while let Some(element) = my_iter.next() {
            let next_element = my_iter.peek();
            total += match (element, next_element) {
                ('I', Some('V')) => -1,
                ('I', Some('X')) => -1,
                ('X', Some('L')) => -10,
                ('X', Some('C')) => -10,
                ('C', Some('D')) => -100,
                ('C', Some('M')) => -100,
                ('I', _) => 1,
                ('V', _) => 5,
                ('X', _) => 10,
                ('L', _) => 50,
                ('C', _) => 100,
                ('D', _) => 500,
                ('M', _) => 1000,
                _ => panic!("Unknown Roman Numeral"),
            }
        }
    return total;
    }
}

//fn main() {
//    let s = String::from("XXVII");
//    let a = roman_to_int(s);
//    println!("{}", a);
//}
