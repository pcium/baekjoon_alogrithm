#include <iostream>
using namespace std;
int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	int N, ct=0;
	cin >> N;
	for(int i=0; i<N; i++) {
		int tmp;
		cin >> tmp;
		if (tmp==1) ct++;
	}
	if(ct>N-ct) cout << "Junhee is cute!";
	else cout << "Junhee is not cute!";
	return 0;
}
