package main

func main() {
	cards := newDeck()

	hand, remaining := deal(cards, 3)
	hand.dprint()
	remaining.dprint()
	cards.saveToFile("mycards") // receiver used to write the deck to the file
}
