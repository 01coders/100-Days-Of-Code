// As a first example of ownership, we’ll look at the scope of some variables

fn demo() {
    // Rust has a first string type, string literal where a string value is hardcoded into our program which are immutable
    // s is string literal and not valid here, it’s not yet declared
    let s = "hello"; // s is valid from this point forward

    // do stuff with s
    // this scope is now over, and s is no longer valid
}

// Rust has a second string type, String. This type is allocated on the heap and as such is able to store an amount of text that is unknown to us at compile time. You can create a String from a string literal using the from function

fn main() {
    demo();
    let mut s = String::from("hello");
    // The double colon (::) is an operator that allows us to namespace this particular from function under the String type

    s.push_str(", world!"); // push_str() appends a literal to a String

    println!("{}", s); // This will print `hello, world!`
    var();
    owner();
    ret_values();
}

// Memory and Allocation in Rust

// In the case of a string literal, we know the contents at compile time, so the text is hardcoded directly into the final executable. This is why string literals are fast and efficient. But these properties only come from the string literal’s immutability.

// With the String type, in order to support a mutable, growable piece of text, we need to allocate an amount of memory on the heap,unknown at compile time, to hold the contents. This means: The memory must be requested from the operating system at runtime. We need a way of returning this memory to the operating system when we’re done with our String.

// That first part is done by us: when we call String::from, its implementation requests the memory it needs.

// However, the second part is different. In languages with a garbage collector (GC), the GC keeps track and cleans up memory that isn’t being used anymore, and we don’t need to think about it. Without a GC, it’s our responsibility to identify when memory is no longer being used and call code to explicitly return it, just as we did to request it. Doing this correctly has historically been a difficult programming problem. If we forget, we’ll waste memory. If we do it too early, we’ll have an invalid variable. If we do it twice, that’s a bug too. We need to pair exactly one allocate with exactly one free.

// Rust takes a different path: the memory is automatically returned once the variable that owns it goes out of scope. Rust calls a special function for us. This function is called drop, and it’s where the author of String can put the code to return the memory. Rust calls drop automatically at the closing curly bracket.

fn var() {
    // Ways Variables and Data Interact: Move [Default]

    // Multiple variables can interact with the same data in different ways in Rust
    let x = 5;
    let y = x; // bind the value 5 to x; then make a copy of the value in x and bind it to y. Now we have x and y, and both equal 5

    let s1 = String::from("hello");
    let s2 = s1; // A String is made up of three parts: a pointer to the memory that holds the contents of the string, a length,                    and a capacity. All this group of data is stored on the stack. The memory on the heap holds the contents of var.

    // When we assign s1 to s2, the String data is copied, meaning we copy the pointer, the length, and the capacity that are on the stack. We do not copy the data on the heap that the pointer refers to. Therefore, any automatic copying can be assumed to be inexpensive in terms of runtime performance.

    // When a variable goes out of scope, Rust automatically calls the drop function. But when s2 and s1 go out of scope, they will both try to free the same memory. This is known as a double free error and Freeing memory twice can lead to memory corruption.

    // In this situation in Rust. Instead of trying to copy the allocated memory, Rust considers s1 to no longer be valid and, therefore, Rust doesn’t need to free anything when s1 goes out of scope.

    // Ways Variables and Data Interact: Clone

    // Rust will never automatically create “deep” copies of your data
    // If we do want to copy the heap data of the String, not just the stack data, we can use a common method called clone.

    let s1 = String::from("hello");
    let s2 = s1.clone();

    // When you see a call to clone, you know that some arbitrary code is being executed and that code may be expensive. It’s a visual indicator that something different is going on.

    // Stack-Only Data: Copy

    let x = 5;
    let y = x;

    // But this code seems to contradict what we just learned: we don’t have a call to clone, but x is still valid and wasn’t moved into y. The reason is that types such as integers that have a known size at compile time are stored entirely on the stack, so copies of the actual values are quick to make.

    // Rust has a special annotation called the Copy which makes older variable usable after assignment
}

// Ownership and Functions
// Passing a variable to a function will move or copy, just as assignment does

fn owner() {
    fn main() {
        // we can use two main func becuse they are under different namespace
        let s = String::from("hello"); // s comes into scope

        takes_ownership(s); // s's value moves into the function...
                            // ... and so is no longer valid here

        let x = 5; // x comes into scope

        makes_copy(x); // x would move into the function,
                       // but i32 is Copy, so it’s okay to still
                       // use x afterward
    } // Here, x goes out of scope, then s. But because s's value was moved, nothing
      // special happens.

    fn takes_ownership(some_string: String) {
        // some_string comes into scope
        println!("{}", some_string);
    } // Here, some_string goes out of scope and `drop` is called. The backing
      // memory is freed.

    fn makes_copy(some_integer: i32) {
        // some_integer comes into scope
        println!("{}", some_integer);
    } // Here, some_integer goes out of scope. Nothing special happens.
    main();
}

// Return Values and Scope
// Returning values can also transfer ownership

fn ret_values() {
    fn main() {
        let s1 = gives_ownership(); // gives_ownership moves its return
                                    // value into s1

        let s2 = String::from("hello"); // s2 comes into scope

        let s3 = takes_and_gives_back(s2); // s2 is moved into
                                           // takes_and_gives_back, which also
                                           // moves its return value into s3
    } // Here, s3 goes out of scope and is dropped. s2 goes out of scope but was
      // moved, so nothing happens. s1 goes out of scope and is dropped.

    fn gives_ownership() -> String {
        // gives_ownership will move its
        // return value into the function
        // that calls it

        let some_string = String::from("hello"); // some_string comes into scope

        some_string // some_string is returned and
                    // moves out to the calling
                    // function
    }

    // takes_and_gives_back will take a String and return one
    fn takes_and_gives_back(a_string: String) -> String {
        // a_string comes into
        // scope

        a_string // a_string is returned and moves out to the calling function
    }
    main();

    // What if we want to let a function use a value but not take ownership? It’s quite annoying that anything we pass in also needs to be passed back if we want to use it again, in addition to any data resulting from the body of the function that we might want to return as well.

    // It’s possible to return multiple values using a tuple

    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{}' is {}.", s2, len);

    fn calculate_length(s: String) -> (String, usize) {
        let length = s.len(); // len() returns the length of a String
        (s, length)
    }
}
