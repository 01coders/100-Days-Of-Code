fn main() {
    type1();
    type2();
    type3();
    type4();
}

fn type1() {
    // Regular Program

    let height: usize = 10;
    let width: usize = 20;

    println!("The area of type1 rectangle is : {}", area(height, width));

    fn area(h: usize, w: usize) -> usize {
        h * w
    }
    //  The width and the height are related to each other because together they describe one rectangle.
    // The area function is supposed to calculate the area of one rectangle, but the function we wrote has two parameters. The parameters are related, but that’s not expressed anywhere in our program. It would be more readable and more manageable to group width and height together.
}

fn type2() {
    // Refactoring with Tuples
    let rectangle: (isize, isize) = (10, 20);

    println!("Area of type2 rectangle is : {}", area(rectangle));

    fn area(dimensions: (isize, isize)) -> isize {
        dimensions.0 * dimensions.1
    }

    // tuples don’t name their elements, so our calculation has become more confusing because we have to index into the parts of the tuple. It would be easy to forget or mix up these values and cause errors, because we haven’t conveyed the meaning of our data in our code.
}

fn type3() {
    // Refactoring with Structs: Adding More Meaning

    struct Rect {
        height: u32,
        width: u32,
    }

    let rect1 = Rect {
        width: 10,
        height: 20,
    };
    println!("Area of type3 rectangle is : {}", area(&rect1));

    // we want to borrow the struct rather than take ownership of it. This way, main retains its ownership and can continue using rect1, which is the reason we use the & in the function signature and where we call the function. This conveys that the width and height are related to each other, and it gives descriptive names to the values rather than using the tuple index values of 0 and 1

    fn area(rectangle: &Rect) -> u32 {
        rectangle.width * rectangle.height
    }
}

fn type4() {
    // Adding Useful Functionality with Derived Traits

    /*
    struct Rectangle {
        width: u32,
        height: u32,
    }

    fn main() {
        let rect1 = Rectangle {
            width: 30,
            height: 50,
        };

        println!("rect1 is {}", rect1);
    }
    */

    // The println! macro by default uses formatting known as Display: output intended for direct end user consumption. The primitive types we’ve seen so far implement Display by default, because there’s only one way you’d want to show a 1 or any other primitive type to a user. But with structs, the way println! should format the output is less clear because there are more display possibilities

    // Putting the specifier :? inside the curly brackets tells println! we want to use an output format called Debug. The Debug trait enables us to print our struct in a way that is useful for developers so we can see its value while we’re debugging our code.

    // Rust does include functionality to print out debugging information, but we have to explicitly opt in to make that functionality available for our struct. To do that, we add the annotation #[derive(Debug)] just before the struct definition
    #[derive(Debug)]
    struct Rectangle {
        width: u32,
        height: u32,
    }

    fn main() {
        let rect1 = Rectangle {
            width: 30,
            height: 50,
        };

        println!("rect1 is {:?}", rect1);
        println!("rect1 is {:#?}", rect1);
    }
    main();
}
