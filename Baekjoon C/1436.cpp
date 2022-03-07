#include <iostream>
using namespace std;

int main(void) {
	int N;
	cin >> N;
	if(N<=6) {
		cout << (N-1)*1000 + 666;
	}
	else if(N>=17) {
		cout << (N-10)*1000 + 666;
	}
	else {
		cout << 6660+(N-7);
	}
	return 0;
}
