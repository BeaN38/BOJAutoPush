#include <stdio.h>

int main() {
    int a, b, c, d, n;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &n);

    if ((a + b + c + d) >= n * 4) {
        printf("%d", 0);
    }
    else {
        printf("%d", n * 4 - (a + b + c + d));
    }

    return 0;
}