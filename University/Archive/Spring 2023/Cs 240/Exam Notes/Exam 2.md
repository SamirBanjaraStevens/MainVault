Coding Problems
## 1
		Create comparator of array; 
			then use qsort
		- Given a array (1-dimensional) use qsort, using a comparator, to sort an array. 
## Notes on question 1
To use qsort function in C to sort an array, we need to provide a comparator function which is used by the qsort algorithm to compare two elements of the array and determine their relative order.

The comparator function takes two `const void *` arguments, which represent the elements to be compared, and returns an `int` value that indicates the relative order of the elements. Specifically, the function should return a negative value if the first element is less than the second, zero if they are equal, or a positive value if the first element is greater than the second.

Here's an example implementation of a comparator function that compares two integers:
```C
int int_compare(const void *a, const void *b) {
    const int *x = (const int *) a;
    const int *y = (const int *) b;
    
    if (*x < *y) {
        return -1;
    } else if (*x == *y) {
        return 0;
    } else {
        return 1;
    }
}
```
To sort an array of integers using `qsort`, we can call the function like this:
```C
int arr[] = {5, 2, 8, 1, 6, 9, 3};
int n = sizeof(arr) / sizeof(int);

qsort(arr, n, sizeof(int), int_compare);
```
In this example, we pass the array `arr` and its size `n` as the first two arguments to `qsort`. The third argument is the size of each element in the array, which in this case is `sizeof(int)`. The fourth argument is the comparator function, which we defined earlier.

After the call to `qsort`, the elements in `arr` will be sorted in ascending order according to the comparator function.

You can modify the comparator function to sort an array of other types, such as characters or strings, by changing the types of the arguments and modifying the comparison logic accordingly.	
# 2 
		Find certain index of an array based on the aggregation of all the elements that come before the index and after the index.
			(Index finding)
## Finding Middle Index:
```C
#include <stdio.h>

int find_middle_index(int arr[], int n) {
    int left_sum = 0;
    int right_sum = 0;
    
    for (int i = 0; i < n; i++) {
        right_sum += arr[i];
    }
    
    for (int i = 0; i < n; i++) {
        right_sum -= arr[i];
        if (left_sum == right_sum) {
            return i;
        }
        if (left_sum < right_sum) {
            left_sum += arr[i];
        } else {
            right_sum += arr[i];
        }
    }
    
    return -1;
}

int main() {
    // example usage
    int arr[] = {1, 2, 3, 4, 2147483647, 2147483647, 4, 3, 2, 1};
    int n = sizeof(arr) / sizeof(int);
    
    int middle_index = find_middle_index(arr, n);
    if (middle_index == -1) {
        printf("No middle index found\n");
    } else {
        printf("Middle index: %d\n", middle_index);
    }
    
    return 0;
}

```
# 3
		Given an array,
			Find the most occurrences of the array item.
				Could be integer or char
					without use of libraries and dictionary
```C
#include <stdio.h>

char most_frequent_char(char arr[], int n) {
    char most_frequent_item = arr[0];
    int max_count = 0;
    
    for (int i = 0; i < n; i++) {
        char item = arr[i];
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (arr[j] == item) {
                count++;
            }
        }
        if (count > max_count) {
            max_count = count;
            most_frequent_item = item;
        }
    }
    
    return most_frequent_item;
}

int most_frequent_int(int arr[], int n) {
    int most_frequent_item = arr[0];
    int max_count = 0;
    
    for (int i = 0; i < n; i++) {
        int item = arr[i];
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (arr[j] == item) {
                count++;
            }
        }
        if (count > max_count) {
            max_count = count;
            most_frequent_item = item;
        }
    }
    
    return most_frequent_item;
}

int main() {
    // example usage
    char char_arr[] = {'a', 'b', 'c', 'a', 'a', 'd', 'b'};
    int int_arr[] = {1, 2, 3, 4, 3, 3, 5, 6};
    int n = sizeof(char_arr) / sizeof(char);
    
    printf("Most frequent char: %c\n", most_frequent_char(char_arr, n));
    printf("Most frequent int: %d\n", most_frequent_int(int_arr, n));
    
    return 0;
}
```

