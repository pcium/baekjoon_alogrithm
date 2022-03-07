#include <iostream>
using namespace std;

int main(void) {
	int num, a=1, b=0, up_a=0, up_b=0;
	cin >> num;
	for(int i=0; i<num; i++) {
		up_a = b;
		up_b = a+b;
		a = up_a;
		b = up_b;
	}
	cout << a << " " << b;
	return 0;
}
