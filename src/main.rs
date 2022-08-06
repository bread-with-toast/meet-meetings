use std::{thread, time};
use std::io;

fn sleep(s: u64) {
    thread::sleep(time::Duration::from_secs(s));
}

pub fn red_text(text: &str) {
    println!("\x1b[31m{}\x1b[0m", text);
}

pub fn green_text(text: &str) {
    println!("\x1b[32m{}\x1b[0m", text);
}

pub fn yellow_text(text: &str) {
    println!("\x1b[33m{}\x1b[0m", text);
}

fn access() {
    let mut purpose = String::new();
    let mut key1 = String::new();
    let mut key2 = String::new();
    let mut key3 = String::new();
    let mut dt = String::new();
    
    println!("Purpose of the meeting: ");
    io::stdin().read_line(&mut purpose).expect("Oh no!");
    sleep(2);

    println!("Key point 1: ");
    io::stdin().read_line(&mut key1).expect("Oh no!");
    sleep(2);

    println!("Key point 2: ");
    io::stdin().read_line(&mut key2).expect("Oh no!");
    sleep(2);

    println!("Key point 3: ");
    io::stdin().read_line(&mut key3).expect("Oh no!");
    sleep(2);

    println!("Date and time of the meeting: ");
    io::stdin().read_line(&mut dt).expect("Oh no!");
    sleep(2);

    yellow_text("\nCopy and paste the information below to the people in your meeting");

    println!("\x1b[44;1m Purpose of the meeting \x1b[0m: {}", purpose);
    println!("\x1b[42;1m Date and time \x1b[0m: {}", dt);
    println!("\x1b[45;1m Key point 1 \x1b[0m: {}", key1);
    println!("\x1b[46;1m Key point 2 \x1b[0m: {}", key2);
    println!("\x1b[41;1m Key point 3 \x1b[0m: {}", key3);
}

fn main() {
    println!("\x1b[35;1m Meet Meetings \x1b[0m");
    sleep(2);

    let mut invite_code = String::new();
    println!("Enter your invite code: ");
    io::stdin().read_line(&mut invite_code).expect("Oh no!");

    if invite_code.trim() == "HKB61M2" {
        green_text("Access granted!");
        sleep(2);
        access();
    } else {
        red_text("Could not grant access!");
        sleep(2);
    }
}
