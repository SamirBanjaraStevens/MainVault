Overflow of Integers'
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

Example code: on a signed integer

```
int main(){
	/*INT_MAX is the maximum representable signed integer*/
	int a = INT_MAX; // 2,147,483,647
	printf("Integer a is equal to : %d\n", a); /* Integer a is equal to : 2,147,483,647 */
	printf("Lets add 5 to a...\n", a); /* Lets add 1 to a... */
	a++;  // Integer a is incremented
	printf(Integer a is equal to : %\n, a); /* Integer a is eaual to : -2,147,483,648 */
	return 0;
}
```

We are trying to add 1 (increment by 1) to INT_MAX. 
But the sum would not fit in the int data type, causing an overflow of an integer.
Thus, resulting in the INT_MIN (minimum value for an int) value. 
	-The resulting output wrapped around the range for a signed int.