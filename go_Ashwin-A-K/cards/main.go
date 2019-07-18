package main

func main() {
	cards := newDeck()

	hand, remaining := deal(cards, 3) // deal func is called and returned values are stored under these two variables
	hand.dprint()                     // they are of type deck. Hence, receiver func is used to print
	remaining.dprint()
}
