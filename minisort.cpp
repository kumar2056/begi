#include <iostream>
using namespace std;
 
int main()
{
int a[10000],e,m;
cin>>e;
for(int i=0;i<e;i++)
{

    cin>>a[i];
}
for(int i=0;i<e;i++)
{
    for(int j=i+1;j<e;j++)
    {
        if(a[i]>a[j])
        {
            m=a[i];
            a[i]=a[j];
            a[j]=m;
        }
    }

  cout<<a[i]<<" ";  
}
