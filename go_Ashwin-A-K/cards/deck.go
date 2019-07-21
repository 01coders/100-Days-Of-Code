package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

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

func deal(d deck, handsize int) (deck, deck) {
	return d[:handsize], d[handsize:]
}

func (d deck) toString() string { // receiver to convert type deck to string
	return strings.Join([]string(d), ",") // join method is used to convert list of strings to one string with a seperator
}

func (d deck) saveToFile(filename string) error { // receiver to write to a file
	return ioutil.WriteFile(filename, []byte(d.toString()), 0666) // writefile func is used to write to a file which takes filename, 																input to be written in terms of byte and file permission as args
}
