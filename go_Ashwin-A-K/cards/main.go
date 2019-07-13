package main

func main() {
	cards := newDeck() // creating variable to store value which is returned from the newDeck func
	cards.dprint()     // receiver func to print values of card
}
