package main

func main() {
	cards := newDeck()

	hand, remaining := deal(cards, 3)
	hand.dprint()
	remaining.dprint()
	cards.saveToFile("mycards")

	cards2 := deckFromFile("mycards") // deck is stored in the var
	cards2.dprint()                   // print new deck
}
