package main

import (
	"sync"
	"fmt"
)

var lock = &sync.Mutex{}

type ATC struct {
}

var instance *ATC;

func GetInstance ()*ATC{
	if instance == nil {
		lock.Lock();
		defer lock.Unlock();
		instance = &ATC{}
	}
	return instance;
}


func main() {
	instance1:=GetInstance();
	instance2:=GetInstance();
	fmt.Println("This will print true if both the instaces are equal",instance1==instance2);
}