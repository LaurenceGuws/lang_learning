use std::io;

fn add(value1: i64, value2: i64) -> i64 {
    value1 + value2
}
fn subtract(value1: i64, value2: i64) -> i64 {
    value1 - value2
}
fn multiply(value1: i64, value2: i64) -> i64 {
    value1 * value2
}
fn divide(value1: i64, value2: i64) -> i64 {
    value1 / value2
}

fn main() {
    let mut operation = String::new();
    println!("Do you want to: add/subtract/multiply/divide ?");
    io::stdin()
        .read_line(&mut operation)
        .expect("Failed to read user input");
    let operation = operation.trim().to_lowercase();

    let mut value1 = String::new();
    println!("Enter your first value");
    io::stdin()
        .read_line(&mut value1)
        .expect("Failed to read first value");
    let value1: i64 = match value1.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("value must be a number");
            return;
        }
    };

    let mut value2 = String::new();
    println!("Enter your second value");
    io::stdin()
        .read_line(&mut value2)
        .expect("Failed to read second value");
    let value2: i64 = match value2.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("value must be a number");
            return;
        }
    };

    let result = match operation.as_str() {
        "add" => add(value1, value2),
        "subtract" => subtract(value1, value2),
        "multiply" => multiply(value1, value2),
        "divide" => divide(value1, value2),
        _ => {
            println!("Unknown operation!");
            return;
        }
    };
    println!("Result: {}", result);
}
