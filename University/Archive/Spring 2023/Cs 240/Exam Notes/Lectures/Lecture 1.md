## Terminal
`ls` ---- lists all files and folders in current directory
`ls - R` ---- displays all files within the current foles and its sub folders recursively
`fs la` --- see permission you have for the current woking directory
`fa sa . system:anyuser none` --- remove all file permesion from any user

##  SHELL SCRIPTING  
Number of shell commands can be combined to create a  program, which we call a shell script that will perform  number of shell commands at the same time. For example, one  can read a file of Andrew ID’s and then create a directory  for each ID in the file. SHELL scripting is a great way to  automate tasks that are too tedious to do manually. We will  discuss more about this in the second half of the course.

## Preprocessing, Compilation, and Linking  
There are 3 major steps to developing a C program.  
	• Editing – The process of creating the source code  
	• Compiling – The process of translating source code to object code  
	• Linking – The process of linking all libraries and  other object codes to generate the executable code

the process of editing allows C programs to be written  using a UNIX editor such as emacs or vim. 

The preprocessing  is performed to replace certain text in the file by others.  
For example:  `#define pi 3.14`  
	The above statement causes C preprocessor to replace all  “pi” references by 3.14. Pi can be referred to as a  “macro”. 

We can also include an external library (that is not part  of the standard libraries) such as “mylibrary.h”.  
`#include “mylibrary.h”`  
`#include <stdio.h> `
Note that the “ “ is used to distinguish external libraries  from standard libraries such as stdio.h.

Compile program
`gcc –ansi myprogram.c`
	- note `-ansi` is s switches that customize the behaviour of the compilation. 
	- Using these switches tells the compiler to apply more scrutiny to your code so that those things which can be detected at compile time will be reported to you as warnings and errors

if the program is syntactically correct, if the proper libraries are available for you to link, then a file called a.out is created. The file a.out is a binary file that can be executed only under the platform the program was  developed in.

to run the program, `./a.out`

