#include <iostream>
using namespace std;

int main(void) {
	
	int a, b, c;

	cin >> a >> b >> c;
	
	int sum;
	sum = a * b * c;

	int arr[10] = { 0, };
	
	for (int i = 0; i < 10; i++) {
		arr[sum % 10]++;
		if(sum > 10) sum /= 10;
		else break;
	}

	for (int i = 0; i < 10; i++) {
		cout << arr[i] << endl;
	}

}