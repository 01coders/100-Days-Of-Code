fn main() {
    // Blocks of code associated with the conditions in if expressions are sometimes called arms,
    // just like the arms in match expressions
    let number = 6;

    if number % 4 == 0 {
        // the condition in if must be a bool
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }

    let condition = true;
    let number = if condition { 5 } else { 6 };
    // if is an expression, we can use it on the right side of a let statement
    // let number = if condition { 5 } else { "six" }; // If the types are mismatched, we’ll get an error.
    // variables must have a single type. Rust needs to know at compile time what type the number variable is, definitively

    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;
        }
    };
    // uses of a loop is to retry an operation you know might fail, such as checking whether a thread has completed its job
    // can add the value you want returned after the break expression you use to stop the loop;
    // that value will be returned out of the loop so you can use it

    let mut number = 3;
    while number != 0 {
        // While a condition holds true, the code runs; otherwise, it exits the loop.
        println!("{}!", number);
        number -= 1;
    }

    let a = [10, 20, 30, 40, 50];
    for element in a.iter() {
        // we’ve now increased the safety of the code and eliminated the chance of bugs that might result from going beyond the end of the array or not going far enough and missing some items.
        println!("the value is: {}", element);
    }
    for number in (1..4).rev() {
        // use Range which is a type provided that generates all numbers in sequence starting from one number
        // and ending before another number and also rev method to reverse the range
        println!("{}!", number);
    }
}
