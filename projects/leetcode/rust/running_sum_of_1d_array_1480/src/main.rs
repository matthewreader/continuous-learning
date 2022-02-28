impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut vec = vec![];
        for i in 0..nums.len() {
            vec.push(nums[0..i+1].iter().sum())
        }
        return vec
    }
}

//fn main() {
//    let a = running_sum(vec![1,2,3,4,5]);
//    println!("{:?}", a);
//}
