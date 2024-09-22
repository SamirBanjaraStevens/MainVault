#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
  int x = 0x7fffffff;
  printf("the x is %d \n", x);
  printf(" the sum is %d \n", x+x); 
  return EXIT_SUCCESS;
}
