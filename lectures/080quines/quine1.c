#include <stdio.h>

int
main (void)
{
  char *s="#include <stdio.h>\n\nint\nmain (void)\n{\n";
  printf(s);  printf("char *s=\"%s\";\n",s);
}
