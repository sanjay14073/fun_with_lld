package main

import (
	"fmt"
	"sync"
);

var lock = &sync.Mutex{}

type single struct {
}

var instance *single

func GetInstance() *single {
	lock.Lock()
	defer lock.Unlock()

	if instance == nil {
		instance = &single{}
	}
	return instance
}

func main() {
	s1 := GetInstance()
	s2 := GetInstance()
	fmt.Printf("Are both instances the same? %v\n", s1 == s2)
}