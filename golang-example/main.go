// Copyright (c) 2014-2017 The btcsuite developers
// Use of this source code is governed by an ISC
// license that can be found in the LICENSE file.

package main

import (
	"log"

	"github.com/btcsuite/btcd/rpcclient"
)

func main() {
	// Connect to local bitcoin core RPC server using HTTP POST mode.
	connCfg := &rpcclient.ConnConfig{
		Host:         "localhost:16124",
		User:         "username",
		Pass:         "mS2SZpPCZZVZwSP8EOCyMmGxqFNyPoKSUdiYSpcLVQE=",
		HTTPPostMode: true, // Bitcoin core only supports HTTP POST mode
		DisableTLS:   true, // Bitcoin core does not provide TLS by default
	}
	// Notice the notification parameter is nil since notifications are
	// not supported in HTTP POST mode.
	client, err := rpcclient.New(connCfg, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Shutdown()

	// Get the current block count.
	blockCount, err := client.GetBlockCount()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Block count: %d", blockCount)

	// Get the current info
	info, err := client.GetInfo()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Version: %d", info.Version)
	log.Printf("Blocks count: %d", info.Blocks)
}
