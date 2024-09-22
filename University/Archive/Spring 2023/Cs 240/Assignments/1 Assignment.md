## **Q1 Unix/Linux Terminal**

- Q 1.1
	- What is the current working directory and how do we get in the terminal?
		- *Solution :*
			- The current working directory (CWD) is the directory or folder we are currently working in in the system.  
			- For example, if we start at the /root directory of the system then our current working directory would be the root directory. But if we type `cd /Applications`, (assuming the directory Applications is within root) then we change into the directory within the root directory called Applications. Now our current working directory is /root/Applications. 
			- To view the path of the current working directory, we can invoke the command `pwd`, which will print the name of the current working directory. 
				- (If we started at root directory and using the `cd` command went into the Applications directory), and we are currently still in the Application directory, and run the `pwd` command, the command line will print `/root/Application`
			- 
- Q 1.2
	- What is the absolute path for a file?
		- *Solution :*
Absolute path 
- is an address that starts from one of two locations:
	- (either "root" (specified with "/" at the beginning of the path) **or** "home" (specified with "~/" at the beginning of the path) )
		- "Full path" - absolute path that starts at "root" with "/", always

- **Q 1.3**
	- What is the relative path for a file?
		- *Solution :*
Relative path
- address that starts from wherever your sitting in the current working directory.
	- For example, In a new terminal session, if we typed the following command,
```
cd /root/data
```
- it would make our current working directory the data directory.
- using the help of a relative path we can enter the file directory without having to using "/", and so we would use the following command:
```
cd file/
```
- then our current working directory would be '/root/data/file'

- **Q 1.4**
	- What is the path variable in the terminal?
		- *Solution :*
PATH variable 
- special variable that contains all of the directories that are automatically searched we attempt to run a program.
	- If we wrote a shell script called `hello.sh` and it's path is for example `/palce/with/the/hello.sh`
	-  function to all of the files in the current working directory that would be executable no matter what the current working directory is. 
		- By adding `/place/with/the` to the `$PATH` variable with the following command:
```
export PATH=$PATH:/place/with/the
```
- `export` : command
- then we are specifying the variable we to set `PATH`.
- Then we are saying we want to set the `PATH` variable to include everything that is already in the path, 
	- by first putting `$PATH`
- Then, we put a colon,
	- that delimits the list of directories in the `PATH` variable.
- Then we specify the location of the file or directory we want accessible from anywhere on the system.
- We will now be able to execute the script `hello.sh` located in `/place/with/the` from anywhere in our system, by typing in the file name without having to include the full path as you type it.
	- This is a temporary sol, because PATH variable will be gone when we close the window.
- *Note :*
	- (PATH) is the variable

- **Q 1.5**
	- How to look up the permissions of the files under the current directory? 
		- *Solution :*
To view permissions of file in the current directory. (or a directory)
- use the command:
```
ls [file_name]
```
- which lists the information about files/directories.
	- adding `-l` to the command returns a long list of information
```
ls -l [file_name]
```
- `ls -l [file name]` is used if we wish to view the permissions of the file or directory in the current working directory. 
	- If we want to look at permissions of a file or directory somewhere else in the system, instead of the file name  `[file_name]` , use the absolute path `/the/place/of/the/file_or_directory`


## **Q2 Integers**

**- Q 2.1**
	- What is the difference between a signed integer and an unsigned integer in C?
		- *Solution :*
		- Firstly, an integer is a variable that represent a real number with no fractional part. Value is stored in binary, because computers cannot represent decimal.  But negative number are real numbers, we represent negative numbers in binary using the most significant bit of a variable to determine its sign. Hence, signed or unsigned integer.
			- Unsigned numbers are always positive or zero, and obey the laws of arithmetic modulo $2^n$. 
				- Where $n$ is the number of bits in the type.
				- and so, unsigned numbers wrap around using modulo. (we will talk about a useful consequence of unsigned numbers in Question 2.3)
			- Unsigned integer uses the leading bit as a part of the value, unlike the signed integer which uses the left-most-bit to determines if the number is positive or negative.
			- Signed numbers, default numerical values, which are both negative and positive, unlike unsigned which can only represent positive numbers. 
			- Because the range of what integer can represent is dependent on the machine, the differences of a signed and unsigned int are shown below according to their machine.
				- 16 bit signed int lie between -32768 and +32767
				- 16 bit unsigned int lie between 0 and +65535
					-  32- bit signed int lie between -2147483648 and 2147483647
					- 32 bit unsigned int lie between 0 and 4294967295 
						- 64 bit signed int lie between $−(2^63)$ and $2^{63 − 1}$.
							- bit of highest significance is reserved for the sign, hence ${63 - 1}$
						- 64 bit unsigned lie between $0$ and $2^{64-1}$

**- Q 2.2**
- (a)
	- How to get the size of an integer variable?
		- *Solution :* 
			- Generally, 
				- the size on an integer is compiler dependent,
					- but the compiler decides weather or not it is also machine dependent. 
				- Using the answer from Question 2.2, lets make a table. 
					- There are 3 types of integers in C

| Type of Integer | Size of **Signed** Integer |
| --------------- | -------------------------- |
| short           | 2 bytes                    |
| int             | 4 bytes                    |
| long            | 8 bytes                    | 

| Type of Integer | Size of **Unsigned** Integer | 
| --------------- | ---------------------------- |
| short           | 2 bytes                      |
| int             | 4 bytes                      |
| long            | 8 bytes                      |

*Note : int is generally 4 bytes even on a 64-bit machine and not 8 bytes (checked on my machine which has a 64-bit processor)*

We can use the operator `sizeof([variable name])`, which yields the size in bytes of its operand.

*Notes : 1 byte = 8 bits*

For example :

```
int a = 32;
printf("\n The size of the integer variable (a) is: %u bytes.", sizeof(a));
return 0;
```

the resulting output
```
The size of the integer variable (a) is : 4 bytes.
```
(b)
	- What's the difference between an int and char?
		- *Solution :*
			- `int` - integer of type int
				- reflects the natural size of the integers on the host machine
					- either 16bits or 32 bits
			- `char` - integer of type char
				- a single byte, capable of holdings one character in the local character set (letters or other characters).
				- So, a char variable is a one-byte integer.
		- The difference is the size in byte of the variable, and the different values the variable can hold.  
			- From our table above, 
				- A *char* occupies exactly one byte, 
					- and accepts values between 0 and 255 unsigned, or -128 and 127 signed.
				- While *int* is **at least** a 2 byte signed word
				- and accepts values between -32767 and 32767 (assuming it is a 2 byte signed word). 

**- Q 2.3**
	- What's the overflow of an integer?
		- *Solution :*
- Arithmetic data types in C have fixed memory storage, hence, there is a fixed maximum value it can store.
	- if the value to be assigned is larger than a variable can hold, it is call integer overflow
		- it will discard those highest bits. (resulting in no error output)
- The implementation of an unsigned integer is a defined behavior,
	- A computation involving unsigned operands can overflow, but does so in a defined behavior, which makes it seem as if it cant overflow. 
		- "A computation involving unsigned operands can never overflow, because a result that cannot be represented by the resulting unsigned integer type is reduced modulo to the number that is one greater than the largest value that can be represented by the resulting type" (C99 standard)
			- unsigned integers can wrap around the maximum value, so the value never crosses the maximum value. 
- however, the over flow of a signed integer is not an implementation-defined behavior ("undefined behavior")
	- the compiler is free to do whatever it sees fit and may produce, useful, unexpected results, or even crash.
		- Generally, in a signed overflow the value is carried over to the sign bit. 
(As shown below for `int a`)

- Can you give an example?
		- *Solution :*
	
Example code: Incrementing a signed and unsigned integer and decrementing a unsigned integer

```
int i;
unsigned int t;

/*Signed Integer Example*/

int a = INT_MAX; /*INT_MAX is the maximum representable signed integer*/
printf("Integer a is equal to : %d\n", a); /* Integer a is equal to : 2,147,483,647 */

printf("Lets add 1 to a...\n", a); /* Lets add 1 to a... */

a++;  // Integer a is incremented

printf(Integer a is equal to : %\n, a); /* Integer a is eaual to : -2,147,483,648 */


/*Unsigned Integer Example*/

t = UINT_MAX; // /*UINT_MAX is the maximum representable unsigned integer*/
t++;
printf("Unsigned integer incremented by one results in : %u\n", t); /*Unsigned integer incremented by one results in : 0*/


t = 0;
printf("Integer t is equal to : %u\n", a); /* Integer t is equal to : 0 */
t--; // Decremening t
printf("After decrementing one, the unsigned integer results in : %u\n", t); /*After decrementing one, the unsigned integer results in : 4,294,967,295*/

```

Summary of code :
We are trying to add 1 (increment by 1) to INT_MAX. 
But the sum would not fit in the int data type, causing an overflow of an integer.
Thus, resulting in the INT_MIN (minimum value for an int) value. 
	- The resulting output wrapped around the range by changing the sign bit.
	- Though if the compiler we utilized was arbitrarily chosen it could've either  produced, useful or unexpected results. Or even crash.
	- 
When we add 1 to UINT_MAX.
The results wrapped around the range from its max to min.

When we subtract an unsigned `int t` representing 0 by 1, the results wraps around from its min to its max.

## **Q3 ASCII Tabel**

**- Q 3.1**
	- How does C store a character type variable?
	- *Solution :*

As mentioned above in solution of Question 2.2. 
- "A character type variable `char` is the size of a single byte, capable of holdings one character in the local character set (letters or other characters). So, a `char` variable is a one-byte integer type."

Through  through the use of  the ASCII numerical code (an encoding system short for "American Standard Code for Information Interchange"). 
- A charter written between single quote represents an integer value equal to the numerical value of the character in the machine's character set. 
	- Called a character constant.
		- For example the character 's' is a character constant 
			- and the ASCII numerical code sets the value of 's' to 115, which is the machine's internal representation of the character 's'.
- For the integer 278 set as a `char` variable `a`
	- the complier coverts 278 from base 10 decimal system to base 2 binary system (100010110).
	- Then, it uses the first 8 bits from the right of the converted binary number. 
		- 1 (00010110)
	- and stores the value 00010110 in the variable char `a`

Example code: 

```
char stringInput[] = "This is a string of charaters";

char myChar = stringInput[7];

print("%c\n", myChar); // Prints 's', stored in the 6th index of the character array

/* Prints 115 corresponding ASCII code for the lowercase character 's' */
print("$d\n", myChar); 

char a = 278;
printf("%d\n", a); // Prints 22
```

Output :
```
main.c: In function ‘main’:
main.c:17:14: warning: overflow in conversion from ‘int’ to ‘char’ changes value from ‘278’ to ‘22’ [-Woverflow]
   17 |     char a = 278;
      |              ^~~
s
115
22
```

*Note :*
- A string of characters is stored as an array of characters

**- Q 3.2**
	- Complete this function, such that it receives a lowercase letter which is guaranteed, and returns an uppercase letter:
- *Solution :*
```
char to_upper(char c){
	if (c >= 'a' && c <= 'z')
		c1 = c - 32;
		return c1;
	else 
		return c;
}
```

## **Q4 Constant Tabel**

- **Q 4.1**
	- Give an integer constant literal of value 20 in its Octal format of the type int.
	- *Solution :*

| Division by $8$ | Quotient | Remainder | Digit# |
| --------------- | -------- | --------- | ------ |
| $\cfrac{20}{8}$ | 2        | 4         | 0      |
| $\cfrac{2}{8}$  | 0        | 2         | 1      | 

Hence, the Octal representation of the integer constant literal 20 in the type int is **024**.

- **Q 4.2**
	- Give an integer constant literal of value 20 in its Hexadecimal format of the type int.
	- *Solution :*

| Division by $16$ | Quotient | Remainder | Digit# |
| ---------------- | -------- | --------- | ------ |
| $\cfrac{20}{16}$ | 1        | 4         | 0      |
| $\cfrac{1}{16}$  | 0        | 1         | 1      | 

Hence, the Hexadecimal representation of the integer constant literal 20 in the type int is  **0X14**

- **Q 4.3**
	- Give a character constant literal of the horizontal tab character of a type of char.
	- *Solution :*
	- 
The horizontal tab escape sequence can be represented as
- '\t' - character /* ASCII horizontal tab */
- '9' - decimal, /* ASCII horizontal tab */
- '\011' - octal /* ASCII horizontal tab */
- '\x9' - hexadecimal /* ASCII horizontal tab */

- **Q 4.4**
	- What is considered the true and false value in C for the if condition statement?
	- *Solution :*
```
if (expression)
	statement1
else
	statement2
```

(else) of if-else is optional depending on your needs. 

The expression is evaluated; 
- If the expression is **true** 
	- expression has a non-zero value
`statement1` is executed
- if expression is **false**
	- expression is zero
if there is an else part `statement2` is executed instead.

Hence, typically 'True' and 'False' correspond to the value 1 and 0 respectively. (Boolean Algebra)



## **Q5 Array**

- **Q 5.1**
	- Complete this function, such that it receives an integer array and its length, and returns the index of the largest number if there are multiple largest numbers return the first one. The length will not exceed the int limits.
- *Solution :*
```C
int arg_max(int nums[], int len){
	// finding the index of the maximum element in the array
	int maxIndex = 0; 
	for (int i = 0; i < len; i++)
	{
		if (nums[i] > nums[maxIndex])
			maxIndex = i;
		for (int j = 0; j < i; j++)
		{
			if (nums[maxIndex] == nums[j])
			{
				break;
			}
		}
	}		
	return maxIndex;
}
```
- two nested loop, outer loops search each element in array for a max,
	- while inner loop searches for a duplicate of the max, if a duplicate is found
		- inner loop breaks
- Q 5.2
	- Given a string in a character array (there's a null character in the end), return the total number of different character that appears. (Do not count the null character). The length will not exceed the int limits.

```C
Example:
s = "abaaa": return 2;
s = "123\n": return 4;

int to_binary(char s[]){
	int count 0;

	for(int i = 0; i < )

}
```

 - *Solution :*

```
int unique_characters(char s[])
{

	/* Divide size of array in bytes by size of each elements in bytes */
	int len = sizeof(s) / sizeof(s[0]);

	// Initilizing counter to 0
	int count = 0;

	for(int i = 0; i < len; i++)
	{
		int flag = 0;
		for (int j = 0; j < i; j++)
		{
			if (s[i] == s[j])
			{
				flag = 1;
				break;
			}
		}
		if (flag == 0)
		{
			count++; // adds 1 to counter every time there is no duplicate
		}
	}
	return count - 1; // subtracted by 1 to account for null character
}
```

First we are given a character array s[]
	- Then, we find the length of the character array and store it as int data type in variable len
		- initialize the integer data type variable count to 0, because we have not counted anything yet.
			- outer loop index the character array from index 0 to len (length of array), incrementing by 1
				- set integer data type variable flag to 0 (false), because we have not flagged any two indexes in array as being a duplicate.
					- inner loop index the character array from 0 to variable i, from outer loop. 
						- the flow of the two nested loops would look like this for the word "apple".

| i                           | j        | s[i] = s[j] ? | flag |                   | Counter                                 |
| --------------------------- | -------- | ------------- | ---- | ----------------- | --------------------------------------- |
| 0 = a                       | 0  = a   | a = a?        | 1    |                   | 0                                       |
|                             |          |               |      | Inner loop breaks |                                         |
|                             |          |               |      |                   |                                         |
| 1 = p                       | 0 = a    | p = a?        |      |                   |                                         |
| 1 = p                       | 1 = p    | p = p?        | 1    |                   |                                         |
|                             |          |               |      | Inner loop breaks |                                         |
|                             |          |               | 0    |                   | 1                                       |
|                             |          |               |      |                   |                                         |
| 2 = p                       | 0 = a    | p = a?        |      |                   |                                         |
| 2 = p                       | 1 = p    | p = p?        | 1    |                   |                                         |
|                             |          |               |      | Inner loop breaks |                                         |
|                             |          |               | 0    |                   | 2                                       |
| 3 = l                       | 0 = a    | l = a?        |      |                   |                                         |
| 3 = l                       | 1 = p    | l = p?        |      |                   |                                         |
| 3 = l                       | 2 = p    | l = p?        |      |                   |                                         |
| 3 = l                       | 3 = l    | l = l?        | 1    |                   |                                         |
|                             |          |               |      | Inner loop breaks |                                         |
|                             |          |               | 0    |                   | 3                                       |
| 4 = e                       | 0 = a    | e = a?        |      |                   |                                         |
| 4 = e                       | 1 = p    | e = p?        |      |                   |                                         |
| 4 = e                       | 2 = p    | e = p?        |      |                   |                                         |
| 4 = e                       | 3 = l    | e = l?        |      |                   |                                         |
| 4 = e                       | 4 = e    | e = e?        | 1    |                   |                                         |
|                             |          |               |      | Inner loop breaks |                                         |
|                             |          |               | 0    |                   | 4                                       |
| 5 = '\n'                    | 0 = a    | '\n' = a?     |      |                   |                                         |
| 5 = '\n'                    | 1 = p    | '\n' = p?     |      |                   |                                         |
| 5 = '\n'                    | 2 = p    | '\n' = p?     |      |                   |                                         |
| 5 = '\n'                    | 3 = l    | '\n' = l?     |      |                   |                                         |
| 5 = '\n'                    | 4 = 2    | '\n' = e?     |      |                   |                                         |
| 5 = '\n'                    | 5 = '\n' | '\n' = '\n'?  | 1    |                   |                                         |
|                             |          |               |      | Inner loop breaks | 5                                       |
| i has reached max of length |          |               |      |                   |  |
Total unique characters in 'apple' is 5, but we subtract by 1 to account for null character. 








