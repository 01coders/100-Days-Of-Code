package main

import "fmt"

type deck []string

func newDeck() deck { // function to create deck
	cards := deck{} // creating slice of type deck
	cardSuits := []string{"Spade", "Club", "Heart", "Diamond"}
	cardValues := []string{"Ace", "Two", "Three"}

	for _, suit := range cardSuits { //iteraing cardSuits
		for _, value := range cardValues { //iterating cardValues
			cards = append(cards, value+" of "+suit) // creating values for cards
		} // underscore is used to ignore the variable as index is not used anywhere
	}
	return cards //returning var
}

func (d deck) dprint() { // function to print deck
	for i, d := range d {
		fmt.Println(i, d) // index and value
	}
}
