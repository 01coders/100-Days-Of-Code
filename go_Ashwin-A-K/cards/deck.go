package main

import "fmt"

type deck []string // custom type funs

func (d deck) dprint() { // (d deck) is a receiver
	for i, d := range d { // receiver sets up methods on the var
		fmt.Println(i, d) // d is copy or instance of variable and deck is variable type
		// thus any variable of type deck can access the receiver func
	}
}
