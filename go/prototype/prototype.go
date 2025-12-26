package main

type Prototype interface {
	Clone() Prototype
}

type Car struct	{
	Brand string
	Model string
	Year  int
}

func (c *Car) Clone() Prototype {
	return &Car{
		Brand: c.Brand,
		Model: c.Model,
		Year:  c.Year,
	}
}

func main() {
	originalCar := &Car{
		Brand: "Toyota",
		Model: "Corolla",
		Year:  2020,
	}
	clonedCar := originalCar.Clone().(*Car)

	println("Original Car:", originalCar.Brand, originalCar.Model, originalCar.Year)
	println("Cloned Car:", clonedCar.Brand, clonedCar.Model, clonedCar.Year)
	 // Modify the cloned car
	clonedCar.Year = 2021
	println("After modification:")
	println("Original Car Year:", originalCar.Year)
	println("Cloned Car Year:", clonedCar.Year)
}