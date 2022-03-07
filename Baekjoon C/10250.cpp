#include <iostream>
using namespace std;

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int rpt;
	cin >> rpt;
	for(int i=0; i<rpt; i++) {
		int H, W, G, floor, number;
		cin >> H >> W >> G;
		floor = G%H;
		if (floor==0) {
			floor = H;
		}
		number = int(G/H) + 1;
		if(G%H==0) {
			number--;
		}
		if(number<10) {
			cout << floor << 0 << number << "\n";
		}
		else {
			cout << floor << number << "\n";
		}
	}
	return 0;
}
