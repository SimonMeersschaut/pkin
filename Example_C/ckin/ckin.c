#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "ckin.h"

#define C_DEG (PI/180.0)
#define P_C      299792458
#define P_E      1.60217733e-19
#define P_EPS0   8.85419e-12
#define C_U      1.6605402e-27  /* Atomic mass to kilograms */
#define C_EV     P_E            /* eV to J */
#define C_BARN   1.0E-28        /* barn  */
#define C_MEV (1.0e6*C_EV)
#define C_NS     1.0e-9
#define C_CM     1.0e-2

/* #define TOFLEN 0.5745 */

#define TOFLEN 0.75541 /* Imec TOF with extension */

/* #define TOFLEN 0.525 */ /* Zagreb */

#define PI M_PI

#define TRUE  1
#define FALSE 0

double Krbs(double,double,double,int);
double Kerd(double,double,double);
double Srbs_mc(double,double,double,double);
double Serd(double,double,double,double,double,double);
int cm_angle(double,double,double *);
double mc2lab_scatc(double,double,double);
double calc_tof(double,double);

double ipow(double,int);
double ipow2(double);
void usage(void);

int main(int argc,char *argv[])
{
   double z1,z2,m1,m2,t,E,Ecm,tcm[2];
   int erd=FALSE,n;
           
   if(argc != 5 && argc !=3)
      usage();

   readparms(argc,argv,&z1,&z2,&m1,&m2);

   m1 *= C_U;
   m2 *= C_U;

   if(argc == 3){
      t = 38.5*C_DEG;
      E = 14.0*C_MEV;
   } else {
      t = atof(argv[3]);
      t *= C_DEG;

      E = atof(argv[4]);
      E *= C_MEV;
   }


   Ecm = m2*E/(m1 + m2);
      
   if(t < PI/2.0)
      erd = TRUE;

   printf("Z1:\t%.0f\n",z1);
   printf("M1:\t%.3f u\n",m1/C_U);

   printf("Z2:\t%.0f\n",z2);   printf("M2:\t%.3f u\n",m2/C_U);

   printf("E:\t%.3f MeV\n",E/C_MEV);
   printf("theta:\t%.3f %c\n",t/C_DEG,248);
   printf("toflen:\t%.2f cm\n",TOFLEN/C_CM);


   n = cm_angle(t,m1/m2,tcm);

   if(n == 0){
      printf("\nScatterered projectiles not detectable\n\n");
   } else if(n == 1) {
      printf("\nRBS(E):     %10.4f MeV\n",E*Krbs(m1,m2,t,0)/C_MEV);
      printf("RBS(tof):   %10.4f ns\n",calc_tof(E*Krbs(m1,m2,t,0),m1)/C_NS);
      printf("RBS(sigma): %10.4f b/sr\n\n",
             mc2lab_scatc(Srbs_mc(z1,z2,tcm[0],Ecm),tcm[0],t)/C_BARN);
   } else {
      printf("\nRBS(E):     %10.4f MeV \t%10.4f MeV\n",
             E*Krbs(m1,m2,t,0)/C_MEV,E*Krbs(m1,m2,t,1)/C_MEV);
      printf("RBS(tof):   %10.4f ns \t%10.4f ns\n",
             calc_tof(E*Krbs(m1,m2,t,0),m1)/C_NS, calc_tof(E*Krbs(m1,m2,t,1),m1)/C_NS);
      printf("RBS(sigma): %10.4f b/sr \t%10.4f b/sr\n\n",
             mc2lab_scatc(Srbs_mc(z1,z2,tcm[0],Ecm),tcm[0],t)/C_BARN,
             -1.0*mc2lab_scatc(Srbs_mc(z1,z2,tcm[1],Ecm),tcm[1],t)/C_BARN);
   }

   if(erd){
      printf("ERD(E):     %10.4f MeV\n",E*Kerd(m1,m2,t)/C_MEV);
      printf("ERD(tof):   %10.4f ns\n",calc_tof(E*Kerd(m1,m2,t),m2)/C_NS);
      printf("ERD(sigma): %10.4f b/sr\n",
      (4.0*Srbs_mc(z1,z2,PI-2*t,Ecm)*cos(t))/C_BARN);
      /*
      printf("ERD(sigma): %10.4f b/sr\n",
          Serd(z1,m1,z2,m2,t,E)/C_BARN);
      */
   } else {
      printf("Recoiled target atoms not detectable\n");
   }

   exit(0);
}
double calc_tof(double energy,double mass)
{
  double value;

  value = TOFLEN/sqrt(2.0*energy/mass);

  return(value);
}
int cm_angle(double lab_angle,double r,double a[])
{
   double stmp;

   if(r > 1.0 && sin(lab_angle) > 1.0/r){
      return(0);
   }

   stmp = asin(r*sin(lab_angle));

   if(r > 1.0) {
      a[0] = lab_angle + stmp;
      a[1] = PI + lab_angle - stmp;
      return(2);
   } else {
      a[0] = lab_angle + stmp;      
      return(1);
   }
   
}
double Krbs(double m1,double m2,double t,int n)
{
   double value,sq_tmp;

   sq_tmp = sqrt(ipow2(m2) - ipow2(m1*sin(t)));

   if(m1 > m2){
      if(n == 0)
         value = ipow2((+sq_tmp + m1*cos(t))/(m1 + m2));
      else
         value = ipow2((-sq_tmp + m1*cos(t))/(m1 + m2));
   } else
         value = ipow2((sq_tmp + m1*cos(t))/(m1 + m2));   

   return(value);
}
double Kerd(double m1,double m2,double t)
{
   double value;
   
   value = (4.0*m1*m2*ipow2(cos(t)))/ipow2(m1 + m2);
   
   return(value);
}
double Srbs_mc(double z1,double z2,double t,double E)
{
   double value;

   value = ipow2((z1*z2*P_E*P_E)/(4.0*PI*P_EPS0))*ipow2(1.0/(4.0*E))*
           ipow(1.0/sin(t/2.0),4);
   return(value);
}
double Serd(double z1,double m1,double z2,double m2,double t,double E)
{
   double value;
     
   value = ipow2(z1*z2*P_E*P_E/(8*PI*P_EPS0*E))*ipow2(1.0 + m1/m2)/
           ipow(cos(t),3);

   return(value);   
}
double mc2lab_scatc(double mcs,double tcm,double t)
{
   double value;
   /*
   printf("tcm: %14.10e\n",tcm);   
   printf("t:   %14.10e\n",t);   
   printf("tcm - t: %14.5e\n",tcm - t);   
   printf("mcs: %14.5e\n",mcs);   
   printf("sin(tcm): %14.5e\n",sin(tcm));   
   printf("sin(t): %14.5e\n",sin(t));
   printf("sin(tcm)/sin(t): %14.5e\n",sin(tcm)/sin(t));   
   */
   value = mcs*ipow2(sin(tcm)/sin(t))/cos(tcm - t);
   /*
   printf("value: %14.5e\n",value);   
   */
   return(value);
}
double ipow2(double x)
{
   return(x*x);
}
double ipow(double x,int a)
{
   double value=1.0;
   int i;
   
   for(i=0;i<a;i++)
      value *= x;

   return(value);
}
void usage(void)
{
   fprintf(stderr,"ckin - calculate scattering energies and cross sections for RBS and ERD\n\n");
   fprintf(stderr,"ckin Z1 Z2 theta(deg) energy(MeV)\n\n");
   fprintf(stderr,"Z1 and Z2 can be given as chemical symbols\n");
   fprintf(stderr,"and they can be preceded by a number of nucleons\n");
          
   exit(1);
}
