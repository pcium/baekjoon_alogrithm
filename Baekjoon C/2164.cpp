#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(void) {
	vector<int> v;
	int N, front=0, back=0;
	cin >> N;
	if (N==1) {
		cout << 1;
		exit(777);
	}
	int *p = new int[N/2];
	for(int i=2; i<=N; i+=2) {
		p[back] = i;
		back++;
	}
	while(1) {
		for(int i=back; i>=0; i--) {
			if(i%2==0) {
				if (i==back) p[i]=0;
				p[i] = p[i+1];
				
			}
		}
		if(v.size()==1) {
			cout << v.at(0);
			exit(0);
		} else if (v.size()==2 || v.size()==3) {
			cout << v.at(1);
			exit(1);	
		}
	}
	return 0;
}
