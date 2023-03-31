#include <stdio.h>

int
main (void)
{
  char *s1="#include <stdio.h>%c%cint%cmain (void)%c{%c";
  char *s2="  char *s1=%c%s%c;%c  char *s2=%c%s%c;%c";
  char n='\n', q='"';
  printf(s1,n,n,n,n,n);
  printf(s2,q,s1,q,n,q,s2,q,n);
}
