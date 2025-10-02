use std::{io};

fn replace_string(str: &str) -> String {
    let mut result = String::new();
    for c in str.chars() {
        match c {
            '<' => result += "&lt;",
            '>' => result += "&gt;",
            '&' => result += "&amp;",
            _ => result += &c.to_string(),
        }
    }
    result
}

fn main() {
    let mut str = String::new();
    io::stdin().read_line(&mut str).unwrap();
    let replaced = replace_string(&str);
    println!("{}", replaced);
}