package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Print("We are running on ")
	arch := runtime.GOARCH
	switch os := runtime.GOOS; os {
	case "darwin": 
		fmt.Println("MacOS, obviously React Andies ... ")
		fmt.Printf("Rocking the %s life \n", arch)

	case "linux":
		fmt.Println("Linux like champs  = 󰋑 -> ")
		fmt.Printf("Rocking the %s life \n", arch)
	
	case "windows":
		fmt.Println("Windows... Life is pain 󰨡 -> ")	
		fmt.Printf("Rocking the %s life \n", arch)
		fmt.Println("Not my fault you don't use nerd fonts.. ")
	
	case "android":
		fmt.Printf("%s like true hackers   󰶤 󰶤 󰶤/n", os)
	default:
		fmt.Printf("%s \n", os)
		fmt.Printf("Rocking the %s life \n", arch)
		fmt.Println("Exotix systems have feelings 2 󱕼")
	}
}
