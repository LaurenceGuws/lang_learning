package main

import "fmt"

func main(){
	// array size if a part of its type, so it cannot change
	var languages [4]string
	languages[0] = "Java"
	languages[1] = "Zig"
	languages[2] = "Rust"
	languages[3] = "Go"
	// languages[4] will not be allowed in the type languages[4]
	fmt.Println(languages[0], languages[1])
	fmt.Println(languages)
	short_lang := [4]string{"Java", "Zig", "Rust", "Go"}
	fmt.Println(short_lang)
}
