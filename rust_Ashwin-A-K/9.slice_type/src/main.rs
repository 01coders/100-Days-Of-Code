fn main() {
    // Another data type that does not have ownership is the slice. Slices let you reference a contiguous sequence of elements in a collection rather than the whole collection

    //  write a function that takes a string and returns the first word it finds in that string
    first_word();
    string_slices();
    slice_as_para();
}

fn first_word() {
    let mut s = String::from("hello world");

    let _word = find_word(&s); // word will get the value 5

    s.clear(); // this empties the String, making it equal to ""

    // word still has the value 5 here, but there's no more string that
    // we could meaningfully use the value 5 with. word is now totally invalid!
    // We could use that value 5 with the variable s to try to extract the first word out, but this would be a bug because the contents of s have changed since we saved 5 in word.

    // Luckily, Rust has a solution to this problem: string slices.

    fn find_word(s: &String) -> usize {
        let bytes = s.as_bytes(); // we’ll convert our String to an array of bytes using the as_bytes method:

        for (i, &item) in bytes.iter().enumerate() {
            // iter is a method that returns each element in a collection and that enumerate wraps the result of iter and returns each element as part of a tuple instead.
            // The first element of the tuple returned from enumerate is the index, and the second element is a reference to the element.
            if item == b' ' {
                return i; // we search for the byte that represents the space by using the byte literal syntax. If we find a space, we return the position. Otherwise, we return the length of the string by using s.len()
            }
        }
        s.len() // else return length of s
    }
}

fn string_slices() {
    let s = String::from("hello world");
    // String slice range indices must occur at valid UTF-8 character boundaries.

    let _hello = &s[0..5];
    let _world = &s[6..11];
    // starting_index is the first position in the slice and ending_index is one more than the last position in the slice.

    let _word = first_word(&s);
    fn first_word(s: &String) -> &str {
        let bytes = s.as_bytes();

        for (i, &item) in bytes.iter().enumerate() {
            if item == b' ' {
                return &s[0..i];
            }
        }

        &s[..]
    }
    /*
    let mut s = String::from("hello world");

    let word = first_word(&s); // here s becomes immutable

    s.clear(); // error because cannot borrow `s` as mutable because it is also borrowed as immutable

    println!("the first word is: {}", word);
    */

    // String Literals Are Slices and both are immutable
}

fn slice_as_para() {
    fn first_word(s: &str) -> &str {
        let bytes = s.as_bytes();

        for (i, &item) in bytes.iter().enumerate() {
            if item == b' ' {
                return &s[0..i];
            }
        }

        &s[..]
    }
    let my_string = String::from("hello world");

    // first_word works on slices of `String`s
    let _word = first_word(&my_string[..]);

    let my_string_literal = "hello world";

    // first_word works on slices of string literals
    let _word = first_word(&my_string_literal[..]);

    // Because string literals *are* string slices already,
    // this works too, without the slice syntax!
    let _word = first_word(my_string_literal);
}
