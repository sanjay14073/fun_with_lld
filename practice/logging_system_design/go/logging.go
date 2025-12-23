package main

import (
	"fmt"
	"sync"
	"log"
)

var lock = &sync.Mutex{}

type Logger struct {
	logger *log.Logger
}

var instance *Logger

func GetInstance() *Logger {
	if instance == nil {
		lock.Lock()
		defer lock.Unlock()

		instance = &Logger{
			logger: log.New(log.Writer(), "ApplicationLogger: ", log.LstdFlags),
		}
	}
	return instance
}

func main() {
	fmt.Println("Logging using singleton pattern");
	logger1:= GetInstance()
	logger1.logger.Println("This is the first log message.")
	logger2:= GetInstance()
	logger2.logger.Println("This is the second log message.")

	if logger1 == logger2 {
		fmt.Println("Both logger instances are the same. Singleton pattern works!")
	} else {
		fmt.Println("Logger instances are different. Singleton pattern failed.")
	}
}