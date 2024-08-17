#include <iostream>
#include <map>
#include <vector>
using namespace std;

void printFrequency(vector<int> v)
{
	// Define an map
	map<int, int> M;
    
    // storing frequency in map
	for(int i:v){
        M[i]++;
    }

    // display frequency
    cout<<"Frequency of elements: "<<endl;
    for(auto pr:M){
        cout<<pr.first<<": "<<pr.second<<"\n";
    }
}

// Driver Code
int main()
{
	int n;
    cout<<"Enter size of array: ";
    cin>>n;

    vector<int>v(n);

    for(int &i:v){
        cin>>i;
    }

    printFrequency(v);
}
