n C, I/O operations can be performed by using the library stdio.h

STDIN – refers to Standard input device (typically a keyboard)  
STDOUT – defines standard output device (typically a termina

**Writing output to STDOUT** 
***
Let us look at `fprintf` first. 
This is a function with variable number of arguments. Here is  
an example.  
`fprintf(STDIN, “This is a test %d %.4f %10.2f %c\n”,134,56.455, 3355.5346, 65);``

**Reading input from STDIN**
***
For example, 
if you need to read  an integer from STDIN
to integer variable x, then you can write;
`scanf(“%d”, &x);`

`fscanf` reads formatted data from a file stream fp and stores them in arguments  
according to the format statement given.

`int fscanf(FILE* fp, const char* format, aorg1, arg2, ...);`

Then you can read two numbers in the file by;  
```C
FILE* fp = fopen(“data.txt”, “r”);  
int x, y;  
fscanf(fp,”%d %d”, &x, &y);
```
