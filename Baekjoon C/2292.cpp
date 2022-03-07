#include <iostream>
using namespace std;

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int hexa_calc, A=1, stage=0, N;
	cin >> N;
	while(1) {
		A = A + 6*stage;
		if (N <= A) break;
		stage++;
	}
	stage++;
	cout << stage; 
	return 0;
}
