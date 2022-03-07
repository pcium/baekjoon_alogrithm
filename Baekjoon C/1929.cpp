#include <iostream>
#include <math.h>
using namespace std;

int main(void) {
	int M, N;
	cin >> M >> N;
	for(int i=M; i<=N; i++) {
		int counter=0;
		for(int j=1; j<=sqrt(i); j++) {
			if(i%j==0) counter++;
		}
		if (counter<=1) cout << i << "\n";
	}
	return 0;
}
