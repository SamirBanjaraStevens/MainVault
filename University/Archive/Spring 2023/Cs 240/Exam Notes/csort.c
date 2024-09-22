#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int parseInt(char*);

int main(int argc, char* argv[]){
  long begin, end;
  int i, j;
  begin = time(NULL);
  printf("%ld\n", begin);
  int n = parseInt(argv[1]);
  int A[n];
  for (i=0;i<n;i++)
    A[i] = random();

  for (i=0; i<n;i++)
    for (j=0; j<n-1;j++)
      if (A[j+1]<A[j])
	{int temp = A[j];
	  A[j] = A[j+1];
	  A[j+1] = temp;
	}
        
  end = time(NULL);
  printf("The elapsed time is %d \n",end-begin);
}

int parseInt(char* s){
  // complete this code
  // note: all strings end with null '\0'
  
  return atoi(s);
}
