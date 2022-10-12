#include<iostream>
#include<ctime>
using namespace std;
int main()
{
    time_t tmNow;
    tmNow = time(NULL);
    struct tm t = *localtime(&tmNow);
    cout<<"Current Date: "<<t.tm_mday<<"-"<<t.tm_mon+1<<"-"<<t.tm_year+1900;
    cout<<endl;
    return 0;
}
