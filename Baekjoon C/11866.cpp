#include <iostream>
using namespace std;

int main(void) {
	int N, K, count_down, hi=0, koong;
	cin >> N >> K;
	int *L = new int[N];
	int *R = new int[N];
	for(int i=0; i<N; i++) {
		L[i]=1;
	}
	count_down=N;
	koong=K;
	while(count_down != 0) {
		hi+=1;
		if(L[(hi-1)%N]!=0) koong--;
		if(koong==0 && L[(hi-1)%N]!=0) {
			if(hi%N==0) 
				R[N-count_down] = N;
			else {
				R[N-count_down] = hi%N;
			}
			L[(hi-1)%N]=0;
			count_down--;
			koong=K;
		}
	}
	cout << "<";
	for(int i=0; i<N-1; i++) cout << R[i] << ", ";
	cout << R[N-1] << ">"; 
	delete[] L;
	delete[] R;
	return 0;
}
