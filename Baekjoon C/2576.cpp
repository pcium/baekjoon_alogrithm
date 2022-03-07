#include <iostream>
using namespace std;
int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	int s[7], sum=0, min=101;
	for(int i=0; i<7; i++) {
		int tmp;
		cin >> tmp;
		if(tmp%2 != 0) {
			sum += tmp;
			if(tmp < min) min = tmp;
		}
	}
	if(sum==0) cout << -1;
	else {
		cout << sum << "\n" << min;
	}
}
