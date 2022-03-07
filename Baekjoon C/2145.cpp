#include <iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int org, divs, acc;
	cin >> org;
	while(org != 0) {
		acc=0;
		divs=1;
		int lime = org%10;
		while(lime != 0 || org/divs != 0) {
			acc += lime;
			divs *= 10;
			lime = org/divs%10;
		}
		if (acc>9) {
			org = acc;
			
			continue;
		}
		else {
			cout << acc << "\n";
			cin >> org;
		}
	}
	return 0;
}
