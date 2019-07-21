package main

import (
	"fmt"
	"os"
)

func main() {
	basicAuth := &BasicAuth{
		Username: os.Getenv("GOROOT"),
		Password: os.Getenv("GOPATH"),
	}
	c := NewRPCClient(os.Getenv("HOME"), basicAuth)
	fmt.Println("ENDPOINT: ", os.Getenv("HOME"))

	address := "my88QLpf2RYYDdNMmDwYvfx6TFc6NXaELa"
	balance, error := c.GetBalance(address)

	if error != nil {
		fmt.Println("GetBalance error: ", error)
	}

	fmt.Println("balance: ", balance) // 0.13514 BTC
}
