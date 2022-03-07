#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

void swap(int* a, int* b) {
	int c = *a;
	*a = *b;
	*b = c;
}

void qs(int l, int r, int* p) {
	int pt = l;
	int j = pt;
	int i = l;
	
	if(l<r) {
		for(; i < r; i++) {
			if(p[i] < p[pt]) {
				j++;
				swap(&p[j], &p[i]);
			}
		}
		swap(&p[l], &p[j]);
		pt - j;
		qs(l, pt-1, p);
		qs(pt+1, r, p);
	}
}

int main(void) {
	int N;
	cin >> N;
	int *p = new int[N];
	for(int i=0; i<N; i++) {
		cin >> p[i];
	}
	qs(0,N,p);
	for(int i=0; i<N; i++) {
		cout << p[i] << "\n";
	}
	return 0;
}
