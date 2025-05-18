package main

import "fmt"

// func add(num1 int, num2 int) int {
// 	return num1 + num2
// }
//When two or more consecutive named function parameters share a type, you can omit the type from all but the last.
func add(num1, num2 int) int {
	return num1 + num2
}

// funcs can return any number of results
func swap(s1, s2 string) (string, string){
	return s2, s1
}

//A return statement without arguments returns the named return values. This is known as a "naked" return.
func concater(str1, str2 string)(concated string){
	concated = str1 + str2
	return
}

func main() {
	fmt.Println(add(22,33))
	fmt.Print(swap("World!\n","Hello "))
	fmt.Println(concater("Hello ","World!"))
}
