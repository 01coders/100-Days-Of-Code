// The terminal emulator is just the window. It runs a text based program, which by default is your login shell (Ex: bash).

// When you type characters in the window, the terminal draws these characters in the window in addition to sending it to the shell’s stdin.

// The characters the shell outputs to stdout and stderr get sent to the terminal, which in turn draws these characters in the window.

fn main() {
    use std::io::{stdin, stdout, Write};
    use std::process::Command; // https://doc.rust-lang.org/std/process/struct.Command.html

    loop {
        print!("fsh> "); // use the `>` character as the prompt
        stdout().flush(); // need to explicitly flush. this to ensure it prints before read_line

        let mut input = String::new(); // Declaring a variable to store user input
        stdin().read_line(&mut input).unwrap(); // reading input from user

        let command = input.trim(); // read_line leaves a trailing newline, which trim removes

        let mut child = Command::new(command) // program gives a path to the program to be executed
            .spawn() // Executes the command as a child process, waiting for it to finish and collecting all of its output
            .unwrap(); // It is should to handle errors

        child.wait().expect("failed to wait on child"); // don't accept another command until this one completes
    }
}
