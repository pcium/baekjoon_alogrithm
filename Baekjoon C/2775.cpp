#include <iostream>
using namespace std;

int fact(int n) {
	if(n==1) return 1;
	return n*fact(n-1);
}

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	int T, k, n, t1=1, t2=1;
	cin >> T;
	for(int i=0; i<T; i++) {
		t1=1, t2=1;
		cin >> k >> n;
		if (n==1) cout << 1 << "\n";
		else {
			for(int j=n; j<=n+k; j++) t1 *= j;
			for(int j=1; j<=k+1; j++) t2 *= j;
			cout << t1/t2 << "\n";
		}
	}
	return 0;
}
