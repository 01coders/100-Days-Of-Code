fn main() {
    // Methods are similar to functions. Methods are different from functions in that they’re defined within the context of a struct or an enum or a trait object and their first parameter is always self, which represents the instance of the struct the method is being called on.

    // Defining Methods
    def_method();
    method_with_params();
    ass_func();
}

fn def_method() {
    struct Rectangle {
        width: i32,
        height: i32,
    }

    // To define the function within the context of Rectangle, we start an impl (implementation) block. Then we move the area function within the impl curly brackets and change the first (and in this case, only) parameter to be self in the signature and everywhere within the body.

    impl Rectangle {
        fn area(&self) -> i32 {
            //  In main, where we called the area function and passed rect1 as an argument, we can instead use method syntax to call the area method on our Rectangle instance.
            self.width * self.height

            //  Methods can take ownership of self, borrow self immutably as we’ve done here, or borrow self mutably, just as they can any other parameter. If we wanted to change the instance that we’ve called the method on as part of what the method does, we’d use &mut self as the first parameter.  this technique is usually used when the method transforms self into something else and you want to prevent the caller from using the original instance after the transformation.
        }
    }

    fn main() {
        let rect = Rectangle {
            width: 10,
            height: 20,
        };
        //  In main, where we called the area function and passed rect1 as an argument, we can instead use method syntax to call the area method on our Rectangle instance.
        println!("Area is : {}", rect.area());
    }
    main();
    // The main benefit of using methods instead of functions, in addition to using method syntax and not having to repeat the type of self in every method’s signature, is for organization. We’ve put all the things we can do with an instance of a type in one impl block rather than making future users of our code search for capabilities of Rectangle in various places in the library we provide.
}

// In C and C++, two different operators are used for calling methods: you use . if you’re calling a method on the object directly and -> if you’re calling the method on a pointer to the object. Rust doesn’t have an equivalent to the -> operator; instead, Rust has a feature called automatic referencing and dereferencing. Rust automatically adds in &, &mut, or * so object matches the signature of the method. It figure out definitively whether the method is reading (&self), mutating (&mut self), or consuming (self)

// Ex: p1.distance(&p2); and (&p1).distance(&p2); are same

fn method_with_params() {
    // we want an instance of Rectangle to take another instance of Rectangle and return true if the second Rectangle can fit completely within self; otherwise it should return false
    fn main() {
        let rect1 = Rectangle {
            width: 30,
            height: 50,
        };
        let rect2 = Rectangle {
            width: 10,
            height: 40,
        };
        let rect3 = Rectangle {
            width: 60,
            height: 45,
        };

        println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
        println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
    }

    struct Rectangle {
        width: u32,
        height: u32,
    }

    impl Rectangle {
        fn area(&self) -> u32 {
            self.width * self.height
        }

        fn can_hold(&self, other: &Rectangle) -> bool {
            // rect1.can_hold(&rect2) passes in &rect2, which is an immutable borrow to rect2, an instance of Rectangle.
            self.width > other.width && self.height > other.height
        }
    }
    main();
}

fn ass_func() {
    // Associated Functions

    // we’re allowed to define functions within impl blocks that don’t take self as a parameter. These are called associated functions because they’re associated with the struct. They’re still functions, not methods, Associated functions are often used for constructors that will return a new instance of the struct.

    #[derive(Debug)]
    struct Rectangle {
        width: u32,
        height: u32,
    }

    // Multiple impl Blocks
    impl Rectangle {
        fn square(size: u32) -> Rectangle {
            Rectangle {
                width: size,
                height: size,
            }
        }
    }

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width > other.width && self.height > other.height
        }
    }

    // To call this associated function, we use the :: syntax with the struct name

    fn main() {
        let sq = Rectangle::square(10);
        println!("{:?}", sq);
    }

    main();
}
