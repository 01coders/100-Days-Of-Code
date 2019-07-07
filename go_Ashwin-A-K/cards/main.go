package main

import "fmt"

func main() {
	// array is of fixed length
	// slice is of variable length

	cards := []string{newcard(), "d1"} // initialize slice in different ways(return from func,hardcoded)
	cards = append(cards, "h6")        //adding value to slice
	fmt.Println(cards)

	for i, card := range cards { // syntax for looping slice
		fmt.Println(i, card) // prints index and value of each card
	}
}

func newcard() string {
	return "c2"
}
