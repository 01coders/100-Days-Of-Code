package main

import "fmt"

func main() {
	// frequently used datatype : bool,string,int,float
	var card string = "d10" // War : go wants to identify the typw on its own
	card1 := "h3"           // it determines the type of variable
	card1 = newcard()            // reassigning var doesn't need ":"
	fmt.Println(card)
	fmt.Println(card1)
}

func newcard() string { // function should have a return type specified after func name
	return "s7" // return type and variable that stores the value should be of same type
}
