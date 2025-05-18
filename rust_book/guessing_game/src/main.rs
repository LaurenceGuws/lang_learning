use rand::Rng;
use std::cmp::Ordering;
use std::io;
fn main() {
    println!("Welcome to the guessing game!");
    /*
    Generate a random number
    */
    let secret = rand::thread_rng().gen_range(1..=10);

    /*
    Loop until the user guesses the secret
    */
    loop {
        /*
        Get user input
        */
        println!("Try to guess the secret (1-10).");
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        /*
        Convert input into a number
        */
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Numbers between 1 and 10 only..");
                continue;
            }
        };

        /*
        Compare input with secret
        */
        match guess.cmp(&secret) {
            Ordering::Less => println!("Too small!!"),
            Ordering::Greater => println!("Too big!!"),
            Ordering::Equal => {
                println!("Nice! You got it this time!!");
                break;
            }
        }
    }
}
