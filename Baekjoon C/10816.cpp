#include <iostream>
using namespace std;

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	int N, M;
	cin >> N;
	int *NO = new int[N];
	for(int i=0; i<N; i++) {
		int tmp;
		cin >> tmp;
		NO[i] = tmp;
	}
	cin >> M;
	int *MA = new int[M];
	for(int i=0; i<M; i++) {
		int tmp, counter=0;
		cin >> tmp;
		for(int j=0; j<N; j++) {
			if(NO[j]==tmp) counter++;
		}
		MA[i] = counter;
		cout << MA[i] << " ";
	}
	return 0;
}

// Timeout -> 트리로 구현해보자 
