package main

import "fmt"

func main(){
	// Slice literals are like array literals without the length
	// This creates an array, then builds a slice that references it
	s1 := []bool{true, false, true, false}
	fmt.Println(s1)

	// This can be done with structs as well
	s2 := []struct {
		b bool
		i int 
	}{
		{true, 1},
		{false, 2},
		{true, 3},
		{false, 4},
	}
	fmt.Println(s2)

	arr1 := [6]int{1, 2, 3, 4, 5, 6}

	// the high and/or low bounds may be omitted when defining a slice, the default will be used for the omitted bound
	// lower bound default = 0, while higher bound default = length of array
	s3 := arr1[:5]
	s4 := arr1[3:]
	s5 := arr1[:]
	fmt.Println(s3, s4, s5)
}
