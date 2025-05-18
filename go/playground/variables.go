package main

import (
	"fmt"
	"math/cmplx"
)

// The var statement declares a list of variables; as in function argument lists, the type is last.
// A var statement can be at package or function level.
var c, python, java bool
func fisrt_print() {
	var i int
	fmt.Println(i, c, python, java)
}

 // A var declaration can include initializers, one per variable.
 // If an initializer is present, the type can be omitted; the variable will take the type of the initializer.
var num1, num2 int = 1, 2
func second_print(){
	var c, python, java = true, false, "no!"
	fmt.Println(num1, num2, c, python, java)
}

// The example shows variables of several types,
// and also that variable declarations may be "factored" into blocks, as with import statements.
// The int, uint, and uintptr types are usually 32 bits wide on 32-bit systems and 64 bits wide on 64-bit systems. 
// When you need an integer value you should use int unless you have a specific reason to use a sized or unsigned integer type. 
// bool
// string
// int  int8  int16  int32  int64
// uint uint8 uint16 uint32 uint64 uintptr
// byte // alias for uint8
// rune // alias for int32
//      // represents a Unicode code point
// float32 float64
// complex64 complex128
var (
	ToBe	bool		= false
	MaxInt	uint64		= 1<<64 - 1
	z		complex128	= cmplx.Sqrt(-5 + 12i)
)

func third_print() {
	fmt.Printf("Type: %T Value %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value %v\n", z, z)

}

func main() {
	fisrt_print()
	second_print()
	third_print()
}
