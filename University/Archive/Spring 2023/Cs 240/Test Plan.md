
# 12 multi-choice
5 points each / 60 points total
***
basic data types; 

char / short / long / double / arrays / structures / unions

how are they reprented; 
constant literal;
array;
headers files;
functions;
block and scope;
initialize a char arary of different ways;  
***

# 4 short-answer
5 points each  / 20 total points each (priority operation) 
***
In C, the priority of an operation determines the order in which it is evaluated in an expression. 

The higher the priority, 
	the earlier the operation is evaluated. 
	
Here are some examples of operations and their priorities in C:

1.  Parentheses: highest priority, evaluated first
2.  Unary operators (e.g. negation, increment, dereference): evaluated second
3.  Multiplicative operators (e.g. multiplication, division, remainder): evaluated third, from left to right
4.  Additive operators (e.g. addition, subtraction): evaluated fourth, from left to right
5.  Relational operators (e.g. less than, greater than): evaluated fifth, from left to right
6.  Equality operators (e.g. equal to, not equal to): evaluated sixth, from left to right
7.  Logical AND: evaluated seventh, from left to right
8.  Logical OR: evaluated eighth, from left to right
9.  Assignment operators: lowest priority, evaluated last

For example, 
	in the expression `a + b * c`, 
		the multiplication operation has a higher priority 
			than the addition operation, 
				so `b * c` is evaluated first, 
					and then the result is added to `a`. 
						If we want to add `a` and `b` first, 
							we can use parentheses to change the order of evaluation: `(a + b) * c`.

It's important to note that the order of evaluation can have a significant impact on the result of an expression, so it's important to use parentheses and understand operator precedence to ensure that expressions are evaluated correctly.


#### Example Questions
*** 
**Q 1 :** What is the result of the following expression, assuming that `a = 2`, `b = 3`, and `c = 4`?
```c
a + b * c
```
Answer: `14` (multiplication has higher priority than addition, so `b * c` is evaluated first, and then added to `a`)
***
**Q 2 :** What is the result of the following expression, assuming that `a = 2`, `b = 3`, and `c = 4`?
```c
(a + b) * c
```
Answer: `20` (parentheses have higher priority than multiplication, so `a + b` is evaluated first, and then multiplied by `c`)
***
**Q 3:** What is the result of the following expression, assuming that `a = 2`, `b = 3`, and `c = 4`?
```c
a * b + c / a
```
Answer: `8` (multiplication and division have the same priority and are evaluated from left to right, so `a * b` is evaluated first, and then `c / a` is evaluated and added to the result)
***
**Q 4:** What is the result of the following expression, assuming that `a = 2`, `b = 3`, and `c = 4`?
```c
a == b || c > b && c < a
```
Answer: `0` (logical AND has higher priority than logical OR, so `c > b && c < a` is evaluated first, but it evaluates to false, so the result is `a == b || false`, which evaluates to `0`)
***
**Q 5 :** What is the result of the following expression, assuming that `a = 2`, `b = 3`, and `c = 4`?
```c
++a * b % c
```
Answer: `2` (prefix increment has higher priority than multiplication and modulus, so `++a` is evaluated first, which increments `a` to `3`, then `3 * b` is evaluated, which is `9`, and finally `9 % c` is evaluated, which is `2`)
***



# 3 coding problems
2 of them 5 points / 1 of them 10 points / 20 total points
***

**Q # 1:** 5 points
***
 
  reverse (orginal order) a string  in-place  (no sorting)

   "AaCcBb": "bBcCaA"

```c
#include <stdio.h>
#include <string.h>

void reverse_string(char* str) {
    int len = strlen(str); // Length of String
    int i;
    char temp;
    for (i = 0; i < len/2; i++) {
        temp = str[i];
        str[i] = str[len-1-i];
        str[len-1-i] = temp;
    }
}

int main() {
    char str[] = "AaCcBb";
    printf("Before: %s\n", str);
    reverse_string(str);
    printf("After: %s\n", str);
    return 0;
}
```
*Notes :* 
We then loop through the first half of the string 
	and swap each character with its corresponding character 
		from the second half of the string. 
			This effectively reverses the string in-place. 
				Note that we only need to loop through the first half of the string 
					since swapping the characters in the second half 
						would just swap them back to their original positions.

**Q # 2:** 5 points
***
reverse the (orignal order) (not the alphabetic) lower letter case letter in that string (no sorting)

  "AaCcBb": "AbCcBa"
  
 ```c
#include <string.h>
#include <ctype.h>

void reverse_lower_case(char *str) {
    int len = strlen(str);
    int i, j;
    char temp;
    for (i = 0, j = len-1; i < j; ) {
        if (islower(str[i]) && islower(str[j])) {
            temp = str[i];
            str[i] = str[j];
            str[j] = temp;
            i++;
            j--;
        }
        else if (!islower(str[i])) {
            i++;
        }
        else if (!islower(str[j])) {
            j--;
        }
    }
}

int main() {
    char str[] = "AaCcBb";
    printf("Before: %s\n", str);
    reverse_lower_case(str);
    printf("After: %s\n", str);
    return 0;
}
```
*Note :*
In this implementation, 
we use the `islower()` function from the `ctype.h` library 
	to check if a character is lowercase. 
	
We then modify the swapping logic 
	so that we only swap two lowercase letters at a time. 
	
The `i` and `j` variables represent the left and right indices of the string respectively, 
	and we loop through the string until they meet in the middle. 
	
If we encounter a non-lowercase letter, 
	we simply increment or decrement the appropriate index without swapping any characters.

**Q # 3:** 10points (2)  
***
given a string, group in-place all lower case letters at the front of the string before any upper case letter, but maintain the original order of all lower/uppers case letters order within

  "AaCcBb":  "acbACB"

  "ACB"  
  "acb"

  
:string in C is just char array

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void group_lower_case(char *str) {
    int len = strlen(str);
    int i, j;
    char temp;
    for (i = 0, j = 0; j < len; j++) {
        if (islower(str[j])) {
            temp = str[i];
            str[i] = str[j];
            str[j] = temp;
            i++;
        }
    }
}

int main() {
    char str[] = "AaCcBb";
    printf("Before: %s\n", str);
    group_lower_case(str);
    printf("After: %s\n", str);
    return 0;
}
```

*Note :*
In this implementation, 
we use the `islower()` function from the `ctype.h` library to check if a character is lowercase. 

We loop through the string with two indices, `i` and `j`, 
	where `i` represents the position where the next lowercase letter should be placed, 
		and `j` represents the position of the next character to be examined. 
		
If the character at `j` is lowercase, 
	we swap it with the character at `i` and increment `i`. 
	
This effectively groups all lowercase letters at the front of the string. 

The uppercase letters will remain in their original order after the lowercase letters.