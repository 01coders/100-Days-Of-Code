// "go run main.go" to compiles and executes the code
// "go build main.go" to compiles the code

/* File structure:
-> package declaration
-> import packages
-> declare function
*/

package main // package(project or workspace) is a collection of common source files.// Main is a executable package
// Other packages are called helper packages which can be dependencies of the main package // They are resuable package

import "fmt" //import gives the package access to the package fmt which is a format lib package

func main() {
	fmt.Println("Hello World")
}


