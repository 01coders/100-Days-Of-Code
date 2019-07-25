package main

import (
	"fmt"
	"io/ioutil"
	"os"
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

func (d deck) toString() string {
	return strings.Join([]string(d), ",")
}

func (d deck) saveToFile(filename string) error {
	return ioutil.WriteFile(filename, []byte(d.toString()), 0666)
}

func deckFromFile(filename string) deck { //func to read from a file
	bs, err := ioutil.ReadFile(filename) // ReadFile func reads content of the file
	if err != nil {                      // error handling
		fmt.Println("Error : ", err)
		os.Exit(1) // terminates the program
	}
	s := strings.Split(string(bs), ",") // converts byte slice to string
	return deck(s)                      // converts string to deck type and returns it
}
