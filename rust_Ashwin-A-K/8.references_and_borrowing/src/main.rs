fn main() {
    reference();
    mut_ref();
    last_used();
    dang();
}

// The issue with the tuple code is that we have to return the String to the calling function so we can still use the String after the call to calculate_length, because the String was moved into calculate_length
// Instead, we reference to an object as a parameter instead of taking ownership of the value

fn reference() {
    fn main() {
        let s1 = String::from("hello");

        let len = calculate_length(&s1);

        // The &s1 syntax lets us create a reference that refers to the value of s1 but does not own it. Because it does not own it, the value it points to will not be dropped when the reference goes out of scope.

        println!("The length of '{}' is {}.", s1, len);
    }

    fn calculate_length(s: &String) -> usize {
        // Likewise, the signature of the function uses & to indicate that the type of the parameter s is a reference
        s.len()
    } // Here, s goes out of scope. But because it does not have ownership of what it refers to, nothing happens.

    main();
    // ampersands are references and they allow you to refer to some value without taking ownership of it
    // The opposite of referencing by using & is dereferencing, which is accomplished with the dereference operator, *
}

// The scope in which the variable s is valid is the same as any function parameter’s scope, but we don’t drop what the reference points to when it goes out of scope because we don’t have ownership.
// When functions have references as parameters instead of the actual values, we won’t need to return the values in order to give back ownership, because we never had ownership.

// Just as variables are immutable by default, so are references. We’re not allowed to modify something we have a reference to.

fn mut_ref() {
    // First, we had to change s to be mut. Then we had to create a mutable reference with &mut s and accept a mutable reference with some_string: &mut String.

    fn main() {
        let mut s = String::from("hello");
        change(&mut s);
    }

    fn change(some_string: &mut String) {
        some_string.push_str(", world");
    }
    main();
    // But mutable references have a restriction:you can have only one mutable reference to a particular piece of data in a particular scope. This code will fail:

    /*
        let mut s = String::from("hello");

        let r1 = &mut s;
        let r2 = &mut s;

        println!("{}, {}", r1, r2);
    */
}

// The benefit of having this restriction is that Rust can prevent data races at compile time

// A data race is similar to a race condition and happens when these three behaviors occur:

// -> Two or more pointers access the same data at the same time.
// -> At least one of the pointers is being used to write to the data.
// -> There’s no mechanism being used to synchronize access to the data.

// And Rust prevents this problem from happening because it won’t even compile code with data races

// A similar rule exists for combining mutable and immutable references. We also cannot have a mutable reference while we have an immutable one
/*
    let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    let r3 = &mut s; // BIG PROBLEM

    println!("{}, {}, and {}", r1, r2, r3);
*/
// However, multiple immutable references are okay because no one who is just reading the data has the ability to affect anyone else’s reading of the data.

// a reference’s scope starts from where it is introduced and continues through the last time that reference is used.
fn last_used() {
    let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    println!("{} and {}", r1, r2);
    // r1 and r2 are no longer used after this point

    let r3 = &mut s; // no problem
    println!("{}", r3);

    // scopes of the immutable references r1 and r2 end after the println! where they are last used, which is before the mutable reference r3 is created.
}

fn dang() {
    // In Rust, by contrast, the compiler guarantees that references will never be dangling references: if you have a reference to some data, the compiler will ensure that the data will not go out of scope before the reference to the data does.

    /*
        fn main() {
            let reference_to_nothing = dangle();
        }

        fn dangle() -> &String { // dangle returns a reference to a String

        let s = String::from("hello"); // s is a new String

        &s  // we return a reference to the String, s
        }   // Here, s goes out of scope, and is dropped. Its memory goes away.
    */

    //  solution here is to return the String directly
}
