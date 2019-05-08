package main

import (
	"fmt"
)

func main() {

	p := fmt.Println

	var a1 []int32

	p(a1)

	a := [3]int64{78, 90, 76}
	p("length of a is", len(a))

	p(a[0], a[1], a[2])

	b := [...]int{12, 78, 50} // ... makes the compiler determine the length

	c := [...]string{"day1", "day2", "day3"}
	p(c[0], c[1], c[2])

	multDimArr := [3][2]string{
		{"00", "01"},
		{"10", "11"},
		{"20", "21"},
	}

	p(multDimArr)
	p(multDimArr[1:3]) //prints [[10 11] [20 21]]

	var slice []int = b[0:3]
	p(slice)

	i := make([]string, 5, 5) //type,len,capacity
	p(i)

	mulDimSlice2 := [][]string{
		{"react", "redux"},
		{"vue", "vuex"},
		{"angular", "rxjs"},
	}

	p(mulDimSlice2)

	if mulDimSlice2[1][0] == "vue" && mulDimSlice2[2][1] == "rxjs" {
		p("condition satisfied")
	}

}
