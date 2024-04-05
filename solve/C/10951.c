#include <stdio.h>

int main() {
    int A, B;
    // scanf는 성공한 스캔값의 개수를 반환
    while (scanf("%d %d", &A, &B) == 2) {
        printf("%d\n", A + B);
    }
    return 0;
}
