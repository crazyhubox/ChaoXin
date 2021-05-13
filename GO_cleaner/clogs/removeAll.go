package clogs

import (
	"fmt"
	"io/ioutil"
	"os"
	"path"
	"time"
)

// const (
// 	LogsDirectory = "/Users/tomjack/Desktop/code/test_for_python2/chaoxin/cx_local/Logger/logs"
// )


// The mode need "all" or "keep"
// The "all" means clean all the log files except today
// The "keep" will kepp the logs in last 3 days.
func RemoveLogs(logsDirectory, mode string) error {
	if mode != "all" && mode != "keep" {
		return fmt.Errorf("%s", "The mode must be the 'all' or 'keep'")
	}

	var logs []string = make([]string, 0)
	timeStr := time.Now().Format("2006-01-02")
	fmt.Println(timeStr)
	logs = GetFiles(logsDirectory, logs)

	if len(logs) == 1 {
		fmt.Println("No logs need to be cleaned.")
	}

	now := time.Now()

	for i := 0; i < len(logs); i++ {
		logFileName := logs[i]
		if filetype, err := checkFilename(logFileName, mode, now); err == nil {
			logsFilePath := fmt.Sprintf("%s/%s", logsDirectory, logFileName)
			if filetype == 1 {
				if err = os.Remove(logsFilePath); err == nil {
					fmt.Printf("%s removed.\n", logFileName)
				}else{
					return err
				}
			}
		}else{
			return err
		}
	}
	return nil
}

func checkFilename(filename string, mode string, now time.Time) (res int, err error) {
	// filename:2021-05-12-sign.log
	// 返回和当前日期的差值,根据模式判断删除返回1,不删返回0, -1有错
	counts, err := countDays(now, filename)
	if err != nil {
		return -1, err
	}

	if mode == "all" && counts != 0 {
		return 1, nil
	}

	if mode == "keep" && counts >= 3 {
		return 1, nil
	}

	return 0, nil
}

func GetFiles(dir string, logs []string) []string {
	if files, err := ioutil.ReadDir(dir); err == nil {
		for i := 0; i < len(files); i++ {
			if files[i].IsDir() {
				logs = GetFiles(files[i].Name(), logs)
			}
			filesuffix := path.Ext(files[i].Name())
			if filesuffix == ".log" {
				logs = append(logs, files[i].Name())
			}
		}
	}
	return logs
}

func countDays(today time.Time, fileName string) (int, error) {

	s, err := time.Parse("2006-01-02", fileName[:10])
	if err != nil {
		return -1, err
	}

	if today.Month() == s.Month() {
		return today.Day() - s.Day(), nil
	}

	currentYear, currentMonth, _ := s.Date()
	currentLocation := s.Location()

	firstOfMonth := time.Date(currentYear, currentMonth, 1, 0, 0, 0, 0, currentLocation)
	lastOfMonth := firstOfMonth.AddDate(0, 1, -1)

	return today.Day() + (lastOfMonth.Day() - s.Day()), nil
}
