package main

import (
	"fmt"
)

func main() {
	primes := [6]int{2 ,3 ,5 ,7 ,11 ,13}
	// A slice is a dynamically-sized, flexible view into the elements of an array.
	// the first element is included, but the lst oone is excluded
	// here index 2 to 4 will be included
	var slice = primes[2:5]
	fmt.Println(slice)

	// slices do not store data, only reference data from an array, so changes to the array/other slices
	// referencing the same data will be reflected in slice
	var slice2 = primes[0:3]
	fmt.Println(slice, slice2)
	primes = [6]int{1, 1, 1, 1, 1, 1}
	fmt.Println(slice, slice2)

}
