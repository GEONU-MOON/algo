#include <stdio.h>
int main() {
	int N = 0, i = 0, j = 0;
	scanf("%d", &N);
	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++){
			if (j <= N - i) printf(" ");
			else printf("*");
		}
		printf("\n");
	}
	return 0;
}