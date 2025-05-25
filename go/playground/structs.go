package main

import "fmt"

type Developer struct {
	// Capitals to make anything publically scoped
	Xp_years int
	Specialty string
	Preferred_lang string
}

func main() {
	fmt.Println(Developer{3, "Integration", "Rust"})

	// use the fields with the . opperator
	me := Developer{3, "Integration", "Rust"}
	me.Preferred_lang = "Zig"
	fmt.Println(me.Preferred_lang)

	// pointers work a bit easier with strucks
	pointer := &me
	// struck pointer values are automatically dereferenced for syntactical sugar 
	// (instead of using '(*pointer).Preferred_lang = "Java"')
	pointer.Preferred_lang = "Java"
	fmt.Println(me)
}
