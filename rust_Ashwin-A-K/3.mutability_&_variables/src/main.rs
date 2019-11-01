fn main() {
    let x = 5; // Variables are immutable only by default
    println!("Value is {}", x);

    //x = 6; error -> cannot assign twice to immutable variable

    let mut y = 6; // 'mut' conveys that variable is immutable
    println!("Value is {}", y);
    y = 7; //  x binds to from 5 to 6 when mut is used
    println!("Value is {}", y);

    //  Rust’s naming convention for constants is to use all uppercase with underscores between
    //  words, and underscores can be inserted in numeric literals to improve readability
    // Constants may be set only to a constant expression, not the result of a function call or
    // any other value that could only be computed at runtime
    const MAX_POINTS: u32 = 100_000; // type of the value must be annotated and _ as a visual separator

    let z = 5;
    let z = z + 1;
    // first variable is shadowed by the second, which means that the second variable’s
    // value is what appears when the variable is used

    // By using let, we can perform a few transformations on a value but have the variable
    // be immutable after those transformations have been completed.

    // The other difference between mut and shadowing is that because we’re effectively
    // creating a new variable when we use the let keyword again, we can change the type of the value but reuse the same name.
}
