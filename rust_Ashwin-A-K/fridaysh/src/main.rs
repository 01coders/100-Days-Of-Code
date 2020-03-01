// The terminal emulator is just the window. It runs a text based program, which by default is your login shell (Ex: bash).

// When you type characters in the window, the terminal draws these characters in the window in addition to sending it to the shell’s stdin.

// The characters the shell outputs to stdout and stderr get sent to the terminal, which in turn draws these characters in the window.

fn main() {
    use std::env;
    use std::io::{stdin, stdout, Write};
    use std::path::Path;
    use std::process::Command; // https://doc.rust-lang.org/std/process/struct.Command.html

    loop {
        print!("fsh> "); // use the `>` character as the prompt
        stdout().flush(); // need to explicitly flush. this to ensure it prints before read_line

        let mut input = String::new(); // Declaring a variable to store user input
        stdin().read_line(&mut input).unwrap(); // reading input from user

        let mut parts = input.trim().split_whitespace(); // everything after the first whitespace character is interpreted as args
                                                         // print!("{:#?}", parts.next());
        let command = parts.next().unwrap(); // https://doc.rust-lang.org/std/iter/trait.Iterator.html#examples
                                             // next() advances the iterator present in "parts" variable and returns the next value
        let args = parts; // It has arguments that are seperated by whitespace

        match command {
            "cd" => {
                let new_dir = args.peekable().peek().map_or("/", |x| *x);
                // peekable() creates a iterator which can use peek to look at the next element of the iterator without consuming it
                // peek() returns a reference value without advancing the iterator
                // default to '/' as new directory if one was not provided
                // map_or() applies a function to the contained value (if any), or returns the provided default (if not)
                let root = Path::new(new_dir);
                if let Err(e) = env::set_current_dir(&root) {
                    eprintln!("{}", e);
                }
            }
            command => {
                let mut child = Command::new(command) // program gives a path to the program to be executed
                    .args(args)
                    .spawn() // Executes the command as a child process, waiting for it to finish and collecting all of its output
                    .unwrap(); // It is should to handle errors

                child.wait().expect("failed to wait on child"); // don't accept another command until this one completes
            }
        }
    }
}
