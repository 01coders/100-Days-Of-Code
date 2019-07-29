package main

func main() {
	cards := newDeck()

	// hand, remaining := deal(cards, 3)
	// hand.dprint()
	// remaining.dprint()
	// cards.saveToFile("mycards")

	// cards2 := deckFromFile("mycards")
	// cards2.dprint()

	cards.shuffle()
	cards.dprint()
}
