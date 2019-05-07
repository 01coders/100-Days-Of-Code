package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("day1")

	a, b := 2, 7

	c := a + b
	println(c)

	var float = 2.3
	fmt.Printf("%T\n", float) //default val float64

	p := fmt.Println

	now := time.Now()
	p(now)

	loc := now.Location()
	p(loc)

	Time() //func sleeps for 3sec

	t := time.Now()
	time_elapsed := t.Sub(now)
	p(time_elapsed)
}

func Time() {
	time.Sleep(2000 * time.Millisecond)

	println("after 2 sec")
	time.Sleep(1000 * time.Millisecond)
}
