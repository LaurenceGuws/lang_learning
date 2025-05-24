package main

import (
	"fmt"
	"math"
	"math/big"
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

func second_print() {
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
//
//	// represents a Unicode code point
//
// float32 float64
// complex64 complex128
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func third_print() {
	fmt.Printf("Type: %T Value %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value %v\n", z, z)
}

// The expression T(v) converts the value v to the type T.
var (
	int1             = 1
	float1           = float64(int1) + 0.888888
	int2             = int64(float1)
	int3             = int64(math.Round(float1))
	undecared_string = "first time its used"
)

func fourth_print() {
	fixed_float := new(big.Float).SetPrec(100).SetFloat64(1)
	fixed_float.Add(fixed_float, big.NewFloat(0.8888888))
	undecared_string_in_func := "it works in here with a := only"
	var string3 string = "sldrkfnskldfm"
	undecared_string_in_func2 := fmt.Sprintf("%d %s", int1, undecared_string_in_func)
	// would be nice if I could add the var reference/name to the printed string... sadness
	fmt.Printf("Type: %T Value %v\n", int1, int1)
	fmt.Printf("Type: %T Value %v\n", float1, float1)
	fmt.Printf("Type: %T Value %v\n", int2, int2)
	fmt.Printf("Type: %T Value %v\n", int3, int3)
	fmt.Printf("Type: %T Value %v\n", undecared_string, undecared_string)
	fmt.Printf("Type: %T Value %v\n", undecared_string_in_func, undecared_string_in_func)
	fmt.Printf("Type: %T Value %v\n", undecared_string_in_func2, undecared_string_in_func2)
	fmt.Printf("Type: %T Value %v\n", fixed_float, fixed_float)
	fmt.Printf("Type: %T Value %v\n", string3, string3)

}

func main() {
	fisrt_print()
	second_print()
	third_print()
	fourth_print()
}
