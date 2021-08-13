#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "ckin.h"
#include "get_element.h"

void readparms(int argc,char *argv[],double *z1,double *z2,
               double *m1,double *m2)
{                          
   double scoef[SCOEF_ROWS][SCOEF_COLS];
   char s[5];
   int Z1,Z2,i=1,j=0,a;
   
      

   readscoef(scoef);
   
   if(isdigit((int) argv[i][0])){
      while(isdigit((int) argv[i][j]) && (argv[i][j])!='\0')
         j++;
      if(argv[i][j] == '\0'){
         Z1 = atof(argv[i]);
         if(Z1 < 1 || Z1 > 92)
            fatal_error(4);
         *m1 = scoef[Z1][3];
      } else {
         strncpy(s,argv[i],(unsigned int) j);
         s[j] = '\0';
         a = atoi(s);
         get_element(argv[i]+j,a,&Z1,m1,scoef);
      }
   } else 
      get_element(argv[i],MAI,&Z1,m1,scoef);

   i++;

   if(i>=argc)
      fatal_error(1);
   j = 0; 

   if(isdigit((int) argv[i][0])){
      while(isdigit((int) argv[i][j]) && (argv[i][j])!='\0')
         j++;
      if(argv[i][j] == '\0'){
         Z2 = atof(argv[i]);
         if(Z2 < 1 || Z2 > 92)
            fatal_error(5);
         *m2 = scoef[Z2][3];
      } else {
         strncpy(s,argv[i],(unsigned int) j);
         s[j] = '\0';
         a = atoi(s);
         get_element(argv[i]+j,a,&Z2,m2,scoef);
      }
   } else 
      get_element(argv[i],NATURAL,&Z2,m2,scoef);
   
   *z1 = (double) Z1;
   *z2 = (double) Z2;

   if(*z1 < 1 || *z1 > 92)
      fatal_error(4);
   if(*z2 < 1 || *z2 > 92)
      fatal_error(5);

}

void get_element(char *s,int a,int *z,double *m,double scoef[][SCOEF_COLS])
{
   FILE *fp;
   char S[3],p[3]="00";
   int N,Z,A,len1,len2,found = FALSE;
   double M;
   
   len1 = strlen(s);
   
   strncpy(p,s,(unsigned int) len1);
   
   if((fp = fopen(F_ELEMENTS,"r")) == NULL){
      fprintf(stderr,"Could not open file %s\n",F_ELEMENTS);
      exit(10);   
   }
  
   while(!found && fscanf(fp,"%i %i %i %s %lf %*f",&N,&Z,&A,S,&M)==5){
      len2 = strlen(S);
      if(strncmp(S,p,(unsigned int) len1) == 0 && len1 == len2 && 
         (a == A || a == MAI || a == NATURAL))
         found = TRUE;
   }
   fclose(fp);

   if(!found){
      switch(a){
         case MAI:
            fatal_error(5);
            break;
         case NATURAL:
            fatal_error(5);         
            break;
         default:
            fatal_error(6);
            break;
      }
   }
    
   switch(a){
      case MAI:
         if(Z < 1.0 || Z > 92)
            fatal_error(5);
         *m = scoef[Z][3];
         break;
      case NATURAL:
         if(Z < 1 || Z > 92)
            fatal_error(5);
         *m = scoef[Z][4];
         break;
      default:
         *m = M/1000000.0;
         break;
   }

   *z = Z;   
  
}

void readscoef(double scoef[][SCOEF_COLS])
{
   FILE *fp;
   int i,j;
   char buf[LINE];
   
   if((fp=fopen(F_SCOEFA,"r")) == NULL){
      fprintf(stderr,"Could not open file %s\n",F_SCOEFA);
      exit(10);
   }

   fgets(buf,LINE,fp);
   fgets(buf,LINE,fp);   

   for(i=1;i<=SCOEF_ROWS;i++)
      for(j=1;j<=SCOEF_ACOLS;j++)
         fscanf(fp,"%lf",&(scoef[i][j]));
         
   fclose(fp);
   
   if((fp=fopen(F_SCOEFB,"r")) == NULL){
      fprintf(stderr,"Could not open file %s\n",F_SCOEFB);
      exit(10);
   }

   fgets(buf,LINE,fp);
   fgets(buf,LINE,fp);   

   for(i=1;i<=SCOEF_ROWS;i++)
      for(j=SCOEF_ACOLS+1;j<=SCOEF_ACOLS + SCOEF_BCOLS;j++)
         fscanf(fp,"%lf",&(scoef[i][j]));
         
   fclose(fp);
   
}
void fatal_error(int get_el_errno)
{
   fprintf(stderr,"      Error: %s\n\n",err_strings[get_el_errno]);
   exit(get_el_errno);
}

