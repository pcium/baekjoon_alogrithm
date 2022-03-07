#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

typedef struct Node *PtrToNode;
typedef PtrToNode Position;
typedef PtrToNode List;

struct Node{
	int x;
	int y;
	Position Next;
};

List MakeEmpty() {
	List L = (List)malloc(sizeof(struct Node));
	L->x=-100001;
	L->y=-100001;
	L->Next = NULL;
	return L;
}

Position Find(int X, int Y, List L) {
	// cout << "Entered Find!! \n";
	Position P;
	P = L;
	if (P->Next = NULL) return P;
	while(1) {
		if (P->Next == NULL) return P;
		if(P->Next->x > X) {
			return P;
		}
		if (P->Next->x == X && P->Next->y > Y) {
			return P;
		}
		P = P->Next;
	}
	return P;
}

List Insert(int X, int Y, List L, Position P1) {
	// cout << "Entered Insert!! \n";
	Position TmpCell = (Position)malloc(sizeof(struct Node));
	TmpCell->x = X;
	TmpCell->y = Y;
	TmpCell->Next = P1->Next;
	P1->Next = TmpCell;
	return L;
} 

int main(void) {
	List L = MakeEmpty();
	Position N = (Position)malloc(sizeof(struct Node));
	Position P2;
	int rpt;
	cin >> rpt;
	int X, Y;
	for(int i=0; i<rpt; i++) {
		cin >> X >> Y;
		Position P1 = Find(X,Y,L);
		L = Insert(X,Y,L,P1);
	}
	P2 = L;
	cout << P2->x << " "<< P2->y << "\n";
	P2 = L->Next;
	cout << P2->x << " "<< P2->y << "\n";
	
	cout << "Now let's print!\n";
	while (P2->Next != NULL) {
		cout << P2->x << " "<< P2->y << "\n";
		P2 = P2->Next;
	}
	cout << "Ending\n";
	return 0;
}
