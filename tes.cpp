#include <iostream>
#include <algorithm>


using namespace std;


int main(){
    int arr[5] = {3,5,2,9,7};

    sort(arr, arr + 5); // Mayor a menor
    sort(arr, arr + 5, greater<int>()); // Menor a mayor

    return 0;
}