struct Solution;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut v = stones.to_owned();
        
        while v.len() > 1 {
            v.sort();
            let x = v.pop();
            let y = v.pop();
            v.push(x.unwrap() - y.unwrap());
            
            //println!("x: {:?}, y: {:?}, v: {:?}", x, y, v);
        }
        
        return match v.len() {
            1 =>  v.pop().unwrap(),
            default => 0,
        };
    }
}