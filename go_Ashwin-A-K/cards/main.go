package main

import "fmt"

func main() {

	cards := deck{newcard(), "d1"}
	cards = append(cards, "h6")
	fmt.Println(cards)

	cards.dprint() // deck type variable calls dprint receiver func
}

func newcard() string {
	return "c2"
}
