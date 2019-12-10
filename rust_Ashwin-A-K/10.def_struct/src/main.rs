fn main() {
    // Structs are pieces of different types and name each piece of data so it’s clear what the values mean
    // To define a struct, use keyword struct and name the entire struct. Then, inside curly brackets, we define the names and types of the pieces of data, which we call fields.
    struct User {
        username: String,
        email: String,
        sign_in_count: u64,
        active: bool,
    }
    //  we create an instance of that struct by specifying concrete values for each of the fields(key: value pairs) to use it.
    let mut user1 = User {
        //  We don’t have to specify the fields in the same order in which we declared them in the struct
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    // To get a specific value from a struct, we can use dot notation.
    user1.active = false; // Note the entire instance must be mutable Rust doesn’t allow us to mark only certain fields as mutable.

    // build_user function returns a User instance with the given email and username. The active field gets the value of true, and the sign_in_count gets a value of 1
    fn build_user(email: String, username: String) -> User {
        User {
            email: email,
            username: username,
            active: true,
            sign_in_count: 1,
        }
    }

    // Using the Field Init Shorthand when Variables and Fields Have the Same Name

    fn build_user_sh(email: String, username: String) -> User {
        User {
            // Because the parameter names and the struct field names are exactly the same, we can use the field init shorthand syntax to rewrite build_user so that we doesn’t have the repetition of email and username again
            email,
            username,
            active: true,
            sign_in_count: 1,
        }
    }
    build_user(user1.email, user1.username);

    // Creating Instances From Other Instances With Struct Update Syntax

    // The syntax .. specifies that the remaining fields not explicitly set should have the same value as the fields in the given instance

    let user2 = User {
        email: String::from("another@example.com"),
        username: String::from("anotherusername567"),
        ..user1
    }; //  The instance in user2 has a different value for email and username but has the same values for the active and sign_in_count fields from user1

    // Using Tuple Structs without Named Fields to Create Different Types

    struct Color(i32, i32, i32);
    struct Point(i32, i32, i32);
    // Tuple structs have the added meaning the struct name provides but don’t have names associated with their fields; rather, they just have the types of the fields.

    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);

    // Each struct you define is its own type, even though the fields within the struct have the same types. For example, a function that takes a parameter of type Color cannot take a Point as an argument, even though both types are made up of three i32 values. Otherwise, tuple struct instances behave like tuples

    // Unit-Like Structs Without Any Fields

    // You can also define structs that don’t have any fields! These are called unit-like structs because they behave similarly to (), the unit type.

    // Ownership of Struct Data

    // struct User owned String type rather than the &str string slice type. This is a deliberate choice because we want instances of this struct to own all of its data and for that data to be valid for as long as the entire struct is valid.

    // It’s possible for structs to store references to data owned by something else, but to do so requires the use of lifetimes. (Lifetimes ensure that the data referenced by a struct is valid for as long as the struct is.)
}
