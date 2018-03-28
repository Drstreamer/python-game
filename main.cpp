#include <iostream>

using namespace std;

int main()
{
    string a;
    string tmp;
    cin>>a;
    for(int i=0; i<a.size(); i++)
    {if (a[i]!='@'){tmp+=a[i];}
    else{break;}}
    tmp+="@gmail.com";
    cout<<tmp;
    return 0;
}
