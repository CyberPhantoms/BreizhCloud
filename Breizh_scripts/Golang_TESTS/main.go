package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	exo1()
	exo2()
	exo3()
}

func exo1() {
	var annee int

	fmt.Printf("Entrez votre année de naissance : ")
	fmt.Scanln(&annee)

	currentYear := time.Now().Year()

	result := currentYear - annee

	fmt.Printf("Vous avez %d ans.\n", result)
}

func exo2() {
	var weights = [5]int{56, 65, 84, 45, 120}
	var sum int

	for i := 0; i < len(weights); i++ {
		sum += weights[i]
	}
	total := sum / len(weights)

	fmt.Printf("La moyenne est de %d kg\n", total)
}

func exo3() {
	var file string

	fmt.Printf("Donnez moi un nom de fichier : ")
	fmt.Scanln(file)

	if _, err := os.Stat(file); err == nil {
		fmt.Printf("Le fichier existe.\n")
	} else {
		fmt.Printf("Le fichier n'existe pas.\n")
	}
}
