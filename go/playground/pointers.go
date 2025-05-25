package main 

import "fmt"

// By default, Go passes arguments by value, it copies them. 
// If you want a function to modify the original value, you must pass a pointer.

func main() {
	i := 42
	// pointer is pointing to the i operand using &i
	// AKA pointer holds the address of the variable i
	pointer := &i
	// reads the value of i using *i
	// AKA reads the value at the memory address stored in pointer (dereferencing)
	fmt.Printf("i/pointer = %d \n", *pointer)
	// set the value of using *i
	// AKA changing the value at the memory address stored in pointer (change i via pointer)
	*pointer = 21
	fmt.Printf("i/pointer = %d \n", i)

	str := "memory value"
	copy_mem_value(str)
	// str will not be changed
	fmt.Println(str)
	reference_mem_value(&str)
	// str will be changed
	fmt.Println(str)
}

func copy_mem_value(copy string) {
	// only actually changing the scoped copy of the value
	copy = copy + " changes"
}

func reference_mem_value(ref *string){
	// Need to use the pointer's value operator because we are using a value, not a string variable
	// AKA Dereferencing the pointer to access and modify the original value
	*ref = *ref + " changes"
}
