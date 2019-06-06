#include <iostream>
using namespace std;
 
int main()
{
int a[10000],m,p;
cin>>p;
for(int i=0;i<p;i++)
{

    cin>>a[i];
}
for(int i=0;i<p;i++)
{
    if(a[0]<=a[i+1])
    {
        m=a[0];
        a[0]=a[i+1];
        a[i+1]=m;
    }
}


cout<<" "<<a[0];
return 0;
}
