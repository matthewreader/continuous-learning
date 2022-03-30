impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut total = 0;
        
        for operation in operations {
            total += match operation.as_str() {
                "X++" => 1,
                "++X" => 1,
                "X--" => -1,
                "--X" => -1,
                _ => panic!("Unknown operation"),
            }
        }
    return total;
    }
}

//fn main() {
//    let b = final_value_after_operations(vec!["--X".to_string(),"X++".to_string(),"X++".to_string()]);
//    println!("{}", b);
//}
