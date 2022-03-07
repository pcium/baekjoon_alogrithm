#include <stdio.h>
#include <stdlib.h>

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
	scanf("%d", &rpt);
	int X, Y, i;
	for(i=0; i<rpt; i++) {
		scanf("%d %d", &X, &Y);
		Position P1 = Find(X,Y,L);
		L = Insert(X,Y,L,P1);
		printf("-------\n");
		printf("%d %d\n", P1->x, P1->y);
		printf("%d %d\n", P1->Next->x, P2->Next->y);
		printf("-------\n");
	}
	P2 = L;
	printf("%d %d\n", P2->x, P2->y);
	P2 = L->Next;
	printf("%d %d\n", P2->x, P2->y);
	
	while (P2->Next != NULL) {
		printf("%d %d\n", P2->x, P2->y);
		P2 = P2->Next;
	}
	printf("Ending\n");
	return 0;
}
