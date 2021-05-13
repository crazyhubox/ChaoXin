package clogs

import (
	"fmt"
	"testing"
	"time"
)

func Test_RemoveLogs(t *testing.T) {
	LogsDirectory := "/Users/tomjack/Desktop/code/test_for_python2/chaoxin/cx_local/Logger/logs"
	if err:= RemoveLogs(LogsDirectory,"all"); err != nil{
		fmt.Println(err)
	}
}

func Test_checkFilename(t *testing.T) {
	testNow,_ := time.Parse("2006-01-02", "2021-05-01")
	if res, err := checkFilename("2021-04-28-sign", "keep", testNow); err == nil {
		fmt.Println(res)
	} else {
		fmt.Println(err)
	}
}
