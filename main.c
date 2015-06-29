#include <stdio.h>
#include <stdlib.h>
#include "tokens.h"
#include "lex.yy.c"


int main( int argc, char **argv ){
    int token;
    char str[] = "fita.in";
    FILE *saida;

    ++argv, --argc;  /* skip over program name */
    
    if ( argc > 0 ) yyin = fopen( argv[0], "r" );
    else{
        printf("./main \"nome do arquivo\"\n");
        exit(1);
    }

    saida = fopen(str, "w");

    token = yylex();

    fprintf(saida,"%i\n",token);
    do{
        token = yylex();
        fprintf(saida,"%i\n",token);
    }while(token!= 0);
    fclose(saida);
    return 0;
}