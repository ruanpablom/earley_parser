/* scanner for a toy Pascal-like language */
     
%{
/* need this for the call to atof() below */
#include <math.h>
%}
     
DIGIT    [0-9]
ID       [A-Za-z][A-Za-z0-9]*

 
%option noyywrap 
%%
     
{DIGIT}+    {return T_INTEGER;}
     
{DIGIT}+"."{DIGIT}* { return T_FLOAT;}

"integer"|"real" {return T_TYPE;} 

"var" {return T_VAR;}     

"if" {return T_IF;}

"or" {return T_OR;}

"and" {return T_AND;}

"then" {return T_THEN;}

"begin" {return T_BEGIN;}

"end" {return T_END;}

"procedure" {return T_PROCEDURE;}

"function" {return T_FUNCTION;}

"while" {return T_WHILE;}

"do" {return T_DO;}

"(" {return T_LPARENT;}

")" {return T_RPARENT;}

";" {return T_ENDINSTRUCTION;}

"Result" {return T_RESULT;}
     
{ID} {return T_ID;}

":=" {return T_ATRIB;}

">"|"<"|">="|"<="|"="|"<>" {return T_COMP;}
 
":" {return T_TYDESIG;} 

"+"|"-"|"*"|"/" {return T_BOPERATOR;}

"&&"|""
     
"{"[^}\n\r]*"}"     /* eat up one-line comments */
     
[ \t\n\r]+          /* eat up whitespace */
     
. {return T_NREC;}
 
%%
     
     
		
		 