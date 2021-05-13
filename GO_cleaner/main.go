package main

import (
	"cleaner/clogs"
	"flag"
	"fmt"
)

var (
	mode      string
	directory string
)

func init() {
	flag.StringVar(&mode, "mode", "all", "clean mode.")
	flag.StringVar(&directory, "folder", ".", "logs directory.")
}

func main() {
	flag.Parse()
	if err := clogs.RemoveLogs(directory, mode); err != nil {
		fmt.Println(err)
	}
}
