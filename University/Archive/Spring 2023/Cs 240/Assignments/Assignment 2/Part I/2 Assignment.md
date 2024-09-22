## **Question 1**

What does argc and argv stand for in the main function below?
```C
int main(int argc, char* argv[])
{
return 0;
}
```
-  `argc`     
	- refers to the number of arguments passed 
-  `argc[]`    
	- pointer array which points to each argument passed to the program  
	- The given example checks for arguments supplied from the command line.``

## **Question 2**

##### Standard IO
**(1)** 
	- How to tell if its the end of stdin steam?
***
In Windows,
`[Control+Z]` is the typical keyboard shortcut to denote the end of file.  and in Linux and Unix it is `[Control+D]`.``

**(2)** - How to redirect a text file to stdin at a terminal? Give an example.
***
  
- We can achieve redirection with `>` or `<`       
- the command `>` file : sends standard output to `<file>         
- `./a.c > new-file.txt`          
- `> new-file.txt`             
- creates a file named `new-file` if it doesn't exist               
- and replaces the content with the new contents of the  `a.c` file when it runs.       
- and the command `<` file : redirect the stdin from a file by <        
- `./a < ../data/ints.txt`         
- the right side of the operand `../data/ints.txt` is set as the standard input to be use the executable

## **Question 3**

Macro
**(1)**
	- How to define a macro in C? Give an example.
***
- A Macro is a fragment of code with a given name.
- And whenever that name is called, it is replaced by the contents of that macro.
- So a macro is defined using a preprocessor directive command such as, `#define`
- There are two types of macros,
- *Object-like macros*
- resemble data objects
- & *Function-like*
- resemble function calls
```C
#define h 6.63 * pow(10, -34) // Planck's Constant
```
- Here we used the token `h` in our program to be replaced with `6.63 * pow(10, -34)`


**(2)**
	- What is used to process a macro?
*** 
- A macro is process by a **preprocessor**
- From the above example we see that `#define` is the preprocessor used to process a macro.
- The `#include` preprocessor is used to include header files to C programs.
- For example,`#include <studio.h>`
- `stdio.h` is a header file
- `#include` is a preprocessor directive that replaces the above line with the contents of `stdio.h` header file.


**(3)**
	- On the terminal, which flag for gcc can be used to see the processed Macros results of a C source file? Give an example.
***
- the following flag,

- `gcc -E main.c // Prints out the preproccessed coed`
- `gcc -S main.c // produce the assembly code main.s`  
- `gcc -C main.c // produce object code main.o (lib file)`  
- `gcc -g main.c // produce executable for debugging`
- `gcc -o main main.c // give a name to the output file`  
- `gcc -Wall main.c // enables all the warnings in GCC`
- `gcc main.c -lm // will link the standard math library`  
- `gcc -l // is linking a library (we will come back to this)`

**(4)**
	- Give an example of macro with arguments
***
```c
#include<stdio.h>

int main() {

// # macro definition

#define PI 3.14

int r; // declaring and initialization the radius of circle

scanf ("%d", &r);

float area = PI * (r * r); // calculating area

printf("The area of your circle is : %f", area);

}
```
