package main

import (
	"fmt"
	"time"
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
		fmt.Printf("%s like true hackers   󰶤 󰶤 󰶤 \n", os)
		fmt.Printf("Rocking the %s life \n", arch)

	default:
		fmt.Printf("%s \n", os)
		fmt.Printf("Rocking the %s life \n", arch)
		fmt.Println("Exotix systems have feelings 2 󱕼")
	}
	hour := time.Now().Hour()
	switch {
	case hour < 12:
		fmt.Println("Why are you up this early???? Go back to bed! 󰒲")
	
	case hour < 17:
		fmt.Println("Its time for codiong and your feeling yourself. You still need small commits ")

	default:
		fmt.Println("Stop over achiving . Nobody cares ")
	}
}
