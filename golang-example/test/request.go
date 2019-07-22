package main

import (
	"fmt"
	"encoding/json"
	"log"
	jsonrpc "github.com/KeisukeYamashita/go-jsonrpc"
)


func main() {
	rpcClient := jsonrpc.NewRPCClient("localhost:16124")
	rpcClient.SetBasicAuth("username", "mS2SZpPCZZVZwSP8EOCyMmGxqFNyPoKSUdiYSpcLVQE=")

	response, _ := rpcClient.Call("getinfo")

	data, err := json.Marshal(response)
	if err != nil {
		log.Fatalf("JSON marshaling failed: %s", err)
	}
	fmt.Printf("%s\n", data)

	if rec, ok := response.Result.(map[string]interface{}); ok {
		for key, val := range rec {
			log.Printf(" [========>] %s = %s", key, val)
		}
	} else {
		fmt.Printf("record not a map[string]interface{}: %v\n", response.Result)
	}
 }