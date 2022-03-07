#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int N, M, dif=300001;
	cin >> N >> M;
	vector<int> v;
	for(int i=0; i<N; i++) {
		int ipt;
		cin >> ipt;
		v.push_back(ipt);
	}
	sort(v.begin(), v.end());
	for(int i=0; i<N-2; i++) {
		for(int j=1; j<N-1; j++) {
			for(int k=2; k<N; k++) {
				if(i==j || i==k || j==k) continue;
				if (v[i]+v[j]+v[k]>M) {
					continue;
				}
				else if (M - (v[i]+v[j]+v[k]) == 0) {
					cout << M;
					exit(0);
				}
				else if (M - (v[i]+v[j]+v[k]) > dif) {
					continue;
				}
				 else {
					dif = M - (v[i]+v[j]+v[k]);	
				}
			}
		}
	}
	cout << M - dif;
	return 0;
}
