use std::cell::RefCell;
use std::collections::hash_map::DefaultHasher;
use std::{
    collections::HashMap,
    hash::{Hash, Hasher},
};

#[derive(Default)]
struct Codec {
    dict: RefCell<HashMap<String, String>>,
}

impl Codec {
    fn new() -> Self {
        Default::default()
    }

    fn encode(&self, longURL: String) -> String {
        let hex_digest = {
            let mut s = DefaultHasher::new();
            longURL.hash(&mut s);
            let s = s.finish();
            format!("{:x}", s)
        };
        self.dict.borrow_mut().insert(hex_digest.clone(), longURL);
        format!("http://tinyurl.com/{}", hex_digest)
    }

    fn decode(&self, shortURL: String) -> String {
        let hex_digest = shortURL.replace("http://tinyurl.com/", "");
        if let Some(a) = self.dict.borrow().get(&hex_digest) {
            return a.clone();
        }
        return "".to_owned();
    }
}

#[test]
fn test() {
    let obj = Codec::new();
    let s: String = obj.encode("https://www.google.com".to_string());
    let d: String = obj.decode(s);

    assert_eq!("https://www.google.com".to_string(), d);
}