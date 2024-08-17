#include <iostream>
#include <vector>
using namespace std;
#define newLine '\n'

int main(){
    int n,m;
    cout<<"Enter size of matrix: ";
    cin>>n>>m;
    
    vector<vector<int>> mat(n, vector<int>(m));

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<"Enter element: ";
            cin>>mat[i][j];
        }
    }

    cout<<"\nYour matrix is: \n";

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<mat[i][j]<<" ";
        }
        cout<<newLine;
    }
}