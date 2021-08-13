#define SCOEF_COLS (54+1)
#define SCOEF_ROWS (93+1)
#define SCOEF_ACOLS 16
#define SCOEF_BCOLS 38

#define MAI 0
#define NATURAL -1

#define F_ELEMENTS "C:/soft/ib_tables/masses.dat"
#define F_SCOEFA "C:/soft/ib_tables/scoef.95a"
#define F_SCOEFB "C:/soft/ib_tables/scoef.95b"

#define max(A,B)  ((A) > (B)) ? (A) : (B)
#define min(A,B)  ((A) < (B)) ? (A) : (B)

#define TRUE  1
#define FALSE 0

#define LINE 250

static const char *err_strings[] = {
    "no error",
    "too few command line parameters",
    "maximum energy smaller than minimum energy",
    "negative energy or velocity",
    "no such ion",
    "no such target",
    "no such isotope",
    "negative or zero step",
    "ion velocity exceeds the velocity of light"
};
void get_element(char *,int,int *,double *,double [][SCOEF_COLS]);
void readscoef(double [][SCOEF_COLS]);
void fatal_error(int );

