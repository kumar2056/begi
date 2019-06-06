#include <iostream>
using namespace std;
 
int main()
{
int b[10000],h,m;
cin>>h;
for(int i=0;i<h;i++)
{

    cin>>b[i];
}
for(int i=0;i<h;i++)
{
    for(int j=i+1;j<h;j++)
    {
        if(b[i]>b[j])
        {
            m=b[i];
            b[i]=b[j];
            b[j]=m;
        }
    }

    
}



cout<<b[h-1];
return 0;
}
