package main 

import "fmt"
// A defer statement defers the execution of a function until the surrounding function returns.
// The deferred call's arguments are evaluated immediately, 
// but the function call is not executed until the surrounding function returns. 
func main() {
	fmt.Println("counting..")
	// Deferred function calls are pushed onto a stack. When a function returns, 
	// Synonym for postpone
	defer fmt.Println("will only print after main code completes")

	for i := 0; i < 10; i++ {
		// deferred calls are executed in last-in-first-out order.
		defer fmt.Println(i)
		fmt.Printf("defer no %d in the loop \n", i)
	}

	fmt.Println("Done with main flow")
}
