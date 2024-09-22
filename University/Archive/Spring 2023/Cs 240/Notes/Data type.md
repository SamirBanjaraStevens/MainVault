Variables : objects
- do not store their type at runtime, 
	- as far as machine code is concerned, there is only untyped memory
- Instead, operations on this data, 
	- Interpret the data as a specific type (as a float or as a pointer)
- So, types are only used by the compiler.


A charter written between single quote represents an integer value equal to the numerical value of the character in the machine's character set. 
- Called a character constant.
	- For example the character constant 'A' is a charter constant 
		- and the ASCII numerical code sets the value of 'A' to 65, which is the machine's internal character of the character A

the value of an integer can be specified in octal or hexadecimal instead of decimal.

A leading `0` (zero) on an integer constant means octal.

a leading `0X` or `0x` means hexadecimal

- for example
	- decimal 31 can be written as 
		- `037` in octal 
		- and `0x1f` or `0X1F` in hex.

- octal and hexadecimal constants may be followed by `L`  to male then **long** 
	- or `U` to make them **unsigned**
		- `0XFUL` is an long unsigned constant with a value of 15 decimal