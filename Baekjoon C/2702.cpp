#include <iostream>
using namespace std;

void mat2(int &a, int &b) {
	if(b != 0) {
		int c = b;
		b = a%b;
		a = c;
		mat2(a,b);
	}
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int nd=1;
	while(nd != 0) {
		
	}
	return 0;
}
