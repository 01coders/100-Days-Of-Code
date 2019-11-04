fn main() {
    // Examples for various data representation
    // Decimal	98_222
    // Hex	0xff
    // Octal	0o77
    // Binary	0b1111_0000
    // Byte (u8 only)	b'A
    // two data type subsets: scalar and compound
    // compiler can usually infer what type we want to use based on the value and how we use it
    // One type to another type using parse
    let guess = String::new();
    let guess: u32 = "42".parse().expect("Not a number!"); // If we don’t add the type annotation here, Rust will display the error

    // signed variant can store numbers from -(2**(n - 1)) to 2**(n - 1) - 1
    // Unsigned variants can store numbers from 0 to 2**(n - 1)

    let x = 1; //  integer types default to i32

    // the isize and usize types depend on the kind of computer your program is running on:
    // 64 bits if you’re on a 64-bit architecture and 32 bits if you’re on a 32-bit architecture

    let x = 2.0; // f64 float type by default
    let y: f32 = 3.0; // explicit f32 type assigning
                      //  The f32 type is a single-precision float, and f64 has double precision

    let t = true; // auto annotation
    let f: bool = false; // with explicit type annotation

    let c = 'z'; // char literals are specified with single quotes, as opposed to string literals, which use double quotes
    let z = 'ℤ'; //  Char type as four bytes
                 // and represents a Unicode Scalar Value, which means it can represent a lot more than just ASCII
    let heart_eyed_cat = '😻';

    let tup: (i32, f64, u8) = (500, 6.4, 1); // A tuple is a general way of grouping together some number of other values with a                                                variety of types into one compound type. Tuples have a fixed length.
    let (x, y, z) = tup; // can use pattern matching to destructure a tuple value
    let five_hundred = tup.0; // can access a tuple element directly by using a period (.) followed by
                              // the index of the value we want to access

    // every element of an array must have the same type and arrays in Rust have a fixed length
    let a = [0, 1, 2, 3, 4];
    let a[isize; 5] = [0, 1, 2, 3, 4]; // write an array’s type by using square brackets including the type of each element, a                                            semicolon, and then the number of elements in the array
    let a = [3; 5]; // This is the same as writing let a = [3, 3, 3, 3, 3];
    let first_a = a[0]; // access elements of an array using indexing,
}
