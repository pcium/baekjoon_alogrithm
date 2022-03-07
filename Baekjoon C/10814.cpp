#include <iostream>
#include <list>
#include <string>
using namespace std;

int main(void) {
	int num;
	string s;
	list<string> l;
	cin >> num;
	for(int i=0; i<num; i++) {
		cin >> s;
		l.push_back(s);
		
	}
	return 0;
}
