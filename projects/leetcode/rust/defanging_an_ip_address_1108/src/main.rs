struct Solution;

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace(".", "[.]")
    }
}

#[test]
fn test() {
    assert_eq!(Solution::defang_i_paddr("1.1.1.1".to_string()), "1[.]1[.]1[.]1");
}