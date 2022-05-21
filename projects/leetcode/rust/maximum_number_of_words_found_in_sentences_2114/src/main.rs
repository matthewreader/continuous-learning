struct Solution;

impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        sentences
        .iter()
        .map(|sentence| sentence.split_whitespace().count())
        .max()
        .unwrap() as i32
    }
}


#[test]
fn test() {
    assert_eq!(
        Solution::most_words_found(vec!["please wait".to_string(), "continue to fight".to_string(), "continue to win".to_string()]),
        3
    );
}
