fn main() {
    //  we can enumerate all possible values, which is where enumeration gets its name.
    enum IpAddrKind {
        V4,
        V6,
    }
    // By defining an IpAddrKind enumeration and listing the possible kinds an IP address can be, V4 and V6

    // Enum Values
    let four = IpAddrKind::V4; // instances created of each of the two variants of IpAddrKind
    let six = IpAddrKind::V6;
    // variants of the enum are namespaced under its identifier, and we use a double colon to separate the two. The reason this is useful is that now both values IpAddrKind::V4 and IpAddrKind::V6 are of the same type: IpAddrKind.

    fn route(ip_kind: IpAddrKind) {} // enum as formal parameters
    route(IpAddrKind::V4); // enum as actual parameters (arguments)

    struct IpAddr {
        kind: IpAddrKind,
        address: String,
    }

    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };

    //  We have two instances of this struct. We’ve used a struct to bundle the kind and address values together, so now the variant is associated with the values of their ip type.

    // We can represent the same concept in a more concise way using just an enum
    enum IpAddr1 {
        V4(String),
        V6(String),
    }

    let home = IpAddr1::V4(String::from("127.0.0.1"));

    let loopback = IpAddr1::V6(String::from("::1"));

    // We attach data to each variant of the enum directly, so there is no need for an extra struct

    enum IpAddr2 {
        V4(u8, u8, u8, u8),
        V6(String),
    } //Another advantage to using enum rather than a struct: each variant can have different types and amounts of associated data.
    let home = IpAddr2::V4(127, 0, 0, 1);

    let loopback = IpAddr2::V6(String::from("::1"));

    struct Ipv4Addr {
        // --snip--
    }

    struct Ipv6Addr {
        // --snip--
    }

    enum IpAddr3 {
        V4(Ipv4Addr),
        V6(Ipv6Addr),
    }
    // This code illustrates that you can put any kind of data inside an enum variant: strings, numeric types, or structs

    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }

    // This enum has four variants with different types:
    struct QuitMessage; // unit struct. // Quit has no data associated with it at all.
    struct MoveMessage {
        x: i32,
        y: i32,
    } // Move includes an anonymous struct inside it.
    struct WriteMessage(String); // tuple struct // Write includes a single String
    struct ChangeColorMessage(i32, i32, i32); // tuple struct // ChangeColor includes three i32 values

    // we’re able to define methods on structs using impl, we’re also able to define methods on enums
    impl Message {
        fn call(&self) {
            // method body would be defined here
        }
    }

    let m = Message::Write(String::from("hello"));
    m.call();

    // The body of the method would use self to get the value that we called the method on. In this example, self will be in the body of the call method when m.call() runs.

    // The Option Enum and Its Advantages Over Null Values

    // The Option type encodes the very common scenario in which a value could be something or it could be nothing.
}
