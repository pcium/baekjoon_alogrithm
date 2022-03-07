#include <iostream>
#include <string.h>
using namespace std;

int main(void) {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int rpt;
	cin >> rpt;
	for(int i=0; i<rpt; i++) {
		int left=0, right=0, open=0, check=1;
		left=0;
		char S[50];
		cin >> S;
		if (strlen(S)%2 != 0) {
			check=0;
		}
		for (int j=0; j<strlen(S); j++) {
			if (S[j]=='(') {
				left++;
				open++;
			}
			else if (S[j]==')') {
				right++;
				open--;
			}
			if (open<0) {
				check=0;
				continue;
			}
		}
		if (left != right) {
			check=0;
		}
		if (check==1) {
			cout << "YES\n";
		}
		else {
			cout << "NO\n";
		}
	}
	return 0;
}
