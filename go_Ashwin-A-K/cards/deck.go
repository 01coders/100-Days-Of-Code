package main

import "fmt"

type deck []string

func newDeck() deck {
	cards := deck{}
	cardSuits := []string{"Spade", "Club", "Heart", "Diamond"}
	cardValues := []string{"Ace", "Two", "Three"}

	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, value+" of "+suit)
		}
	}
	return cards
}

func (d deck) dprint() {
	for i, d := range d {
		fmt.Println(i, d)
	}
}

func deal(d deck, handsize int) (deck, deck) { //func that takes card deck and handsize as params and returns 2 deck values
	return d[:handsize], d[handsize:] // range in slices to split the card deck for deal
	// range is similar to python
}
