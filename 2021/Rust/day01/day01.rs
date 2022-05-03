use std::fs;

fn main() {
    let filename = "../../inputs/day01.txt";
    let contents = fs::read_to_string(filename);
    println!("{:?}", contents);
}