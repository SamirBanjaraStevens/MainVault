# C programing topics
1. The meaning of a pointer, *, **, ***  

In C programming, 
	a pointer is a variable that holds the memory address of another variable. (adress in the memory)
The pointer variable itself is stored in memory, 
	and its value is the address of the variable it points to.
	(provides durect access to memory location through its adress)

The `*` operator in C is used in two different ways:

To declare a pointer variable: 
When `*` is used in a variable declaration, 
	it means that the variable is a pointer. 
	
For example, 
the following code declares a pointer variable named `ptr` that can point to an integer:

```c
int *ptr;
```

1. Octal, decimal and hexadecimal  

Conversion code in data spell

-   **Octal:** Octal numbers are base-8 numbers, meaning they use 8 digits: 0, 1, 2, 3, 4, 5, 6, and 7. In C, you can represent an octal number by prefixing it with a `0` (zero) followed by the digits of the number. For example, the octal number 12 is represented as `014` in C.
***
- In C, octal numbers are typically stored as `int` or `unsigned int` data types, which are usually 4 bytes (32 bits) on most modern systems. This means that an octal number can be represented using up to 11 digits, since each digit represents 3 bits (2^3=8) and 11 digits can represent up to 33 bits.


-   **Decimal:** Decimal numbers are base-10 numbers, meaning they use 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. In C, you can represent a decimal number simply by writing its digits, without any prefix or suffix.
***
-  In C, decimal numbers are typically stored as `int`, `long`, or `double` data types, which can vary in size depending on the system architecture and the compiler. For example, on a 32-bit system, an `int` is usually 4 bytes (32 bits), while on a 64-bit system, an `int` is usually 8 bytes (64 bits). This means that the range of values that can be represented by a decimal number depends on the data type used to store it.


-   **Hexadecimal:** Hexadecimal numbers are base-16 numbers, meaning they use 16 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F (where A-F represent the decimal numbers 10-15). In C, you can represent a hexadecimal number by prefixing it with `0x` or `0X` followed by the digits of the number. For example, the hexadecimal number AB is represented as `0xAB` or `0XAB` in C.
***
- In C, hexadecimal numbers are typically stored as `int` or `unsigned int` data types, which are usually 4 bytes (32 bits) on most modern systems. This means that a hexadecimal number can be represented using up to 8 digits, since each digit represents 4 bits (2^4=16) and 8 digits can represent up to 32 bits.

1. Arrays and pointers  

# reading strings 

A C string is an arry of characters ending with a NULL character `\0`

We can allocate stattic memory for a string with

`char s[50];`

this will allocate 50 bytes for the string
and the maximim size of the string that can be stores is 49.

However this is not efficent when a string size is a variable (like in a dictionary)

Thus we can allocate memory using malloc

so if we know the size of a string, say n bytes, we can allocate memory using, 

```C
char* s = (char*)malloc(n+1);
```

we still need to copy the charaters into S.

So we would read a string into a temp array as 

```C
char temp[50];
fscanf(stdin, "%s", tmp);
```
and suppose we need to copy the string to a permanent location. 

```C
char* name = malloc(strlen(tmp)+1);
strcpy(name, tmp);
```

**BUT** 

C arrays can be of any type.
We can define an array of pointers as follows,
Here is the code to define an array of (n) char pointers

```C
char* A[n];
```
Each cell in the array `A[i]` is a `char*` 
and so it can point to a character 

we should initialize all the pointers (or `char*`) to `NULL` with

```C
for (i=0; i<n; i++)
	A[i] = NULL;
```
Assign a string to each `A[i]` 

```C
A[i] = malloc(length_of_string + 1);
```
Array of size n has indices from 0 to n-1
A character can be represented by an integer (ASCII  
value) and can be used as such.
The unary operator & produces an address  
The unary operator * dereference a pointer

1. Function and passing arguments. Why pass addresses?  
2. Linked lists and hash tables ‐ fundamentals  
3. malloc, calloc and free  
4. type of errors caused by a C program and how to detect it  
a. unallocated memory  
b. returning pointers to local variables  
c. dereferencing uninitialized or unallocated memory  
d. confusing pointer and reference types  
e. array index out of bounds  
f. double free of memory  
8. Writing C macros and how they are processed?  
9. macro vs typedef and macros vs functions  
10. bit operations, getbit, setbit, masking  
11. Missing libraries, what can go wrong?  
12. Writing Make files and why write make files?  
13. Finding memory leaks with valgrind. What causes memory leaks?  
14. Debugging with gdb  
15. Function pointers, typedef’s and applications  
16. void*’s and how to use them in developing generic libraries  
17. using qsort, how to write a comparator  
18. The difference between an array and a pointer? * vs [] , ** vs [][] etc..  
19. Systems programming with C  
	a. File operations – open, creat, read, close, write, mkdir, rmdir etc  
	b. Process operations – fork, exec, wait/waitpid, exit,  
20. Optimizing code – manually, with gcc flags

# Misc
1. C and assembly  
2. How programs get compiled  
3. How programs get loaded and executed  
4. Instruction Set Architecture  
5. Hypothetical SAMS machine  
6. Writing an assembly program for SAMS  
7. Thinking about SAMS assembler and simulator