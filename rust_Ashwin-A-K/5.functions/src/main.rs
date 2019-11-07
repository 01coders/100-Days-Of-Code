fn main() {
    another_func(5, 6.8);
    println!("Hello, world!");
    another_function();

    // Statements are instructions that perform some action and do not return a value. Expressions evaluate to a resulting value
    //  x = y = 6 and have both x and y have the value 6; that is not the case in Rust.
    // Calling a function is an expression. Calling a macro is an expression.
    // The block that we use to create new scopes, {}, is an expression.

    let x = 5;
    let y = {
        x + 1 // Note the x + 1 line without a semicolon at the end, Expressions do not include ending semicolons.
              // If you add a semicolon to the end of an expression, you turn it into a statement, which will then not return a         value.
    };
    let x = plus_one(5);
}

// Rust doesn’t care where you define your functions, only that they’re defined somewhere.

fn another_function() {
    // Rust code uses snake case as the conventional style for function and variable names
    println!("Another Function");
}

fn another_func(x: isize, y: f64) {
    // example creates a function with two parameters, both of which are isize and f64 type
    println!("{} {}", x, y);
}

fn plus_one(x: i32) -> i32 {
    // We don’t name return values, but we do declare their type after an arrow (->)
    x + 1
    // return value of the function is the value of the final expression in the block of the body of a function
    // You can return early from a function by using the return keyword and specifying a value,
    // but most functions return the last expression implicitly

    // But if we place a semicolon at the end of the line containing x + 1, changing it from an expression to a statement, we’ll get an error saying “mismatched types”. Statements don’t evaluate to a value, which is expressed by (), an empty tuple. Therefore, nothing is returned, which contradicts the function definition and results in an error.
}
