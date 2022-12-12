/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;
double converter(double celcius){
    return celcius*1.8+32 ;

}


int main()
{ 
    double number; 
    number= converter(56.7);
    if (number>100){
        for (int i = 0 ; i<5; i++){
            cout<<number<<endl;
            
        }
        }
    cout<<"Hello World"<<endl;

    return 0;
    
}

