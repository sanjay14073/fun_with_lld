package main

import "fmt"

type House struct {
	color          string
	noOfFloors     int
	modularKitchen bool
	interiorDesign bool
}

type HouseBuilder struct {
	color          string
	noOfFloors     int
	modularKitchen bool
	interiorDesign bool
}

func (b *HouseBuilder) AddColor(color string) *HouseBuilder {
	b.color = color
	return b
}

func (b *HouseBuilder) AddFloors(floors int) *HouseBuilder {
	b.noOfFloors = floors
	return b
}

func (b *HouseBuilder) AddModularKitchen() *HouseBuilder {
	b.modularKitchen = true
	return b
}

func (b *HouseBuilder) AddInteriorDesign() *HouseBuilder {
	b.interiorDesign = true
	return b
}

func (b *HouseBuilder) Build() House {
	return House{
		color:          b.color,
		noOfFloors:     b.noOfFloors,
		modularKitchen: b.modularKitchen,
		interiorDesign: b.interiorDesign,
	}
}

func main() {
	builder := &HouseBuilder{}

	house := builder.
		AddColor("Blue").
		AddFloors(2).
		AddModularKitchen().
		AddInteriorDesign().
		Build()

	fmt.Print(house);
}