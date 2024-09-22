
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define undefined -1

int pow(int x, int y){
  if (y==0) return 1;
  else
    return x*pow(x,y-1);
} 


/* what does this function returns? */
int foo(int x, int y){
  int r = 1;
  while (y > 0) {
    if (y%2) r=r*x;
    x = x*x;
    y = y/2;
  }
  return r;
}


int main(int argc, char* argv[]){

  assert(foo(2,2)==4);
  assert(foo(2,0)==1);
  assert(foo(2,3)==8);  
  return EXIT_SUCCESS;
}
