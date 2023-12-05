#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <sys/ucontext.h>

#define AOC_LOG 1
#include "common.h"

int main(void) {
    FILE *file = fopen("content/day_1.txt", "rb");

    if (!file) {
        elog(stderr, "ERROR: Unable to open file\n");
        return 1;
    }

    char d;
    char f = '0', l = '0';
    long sum = 0;
    while (!((d = getc(file)) == EOF)) {
        if (d == '\n') {
            int value = (f - '0') * 10 + (l - '0');
            sum += value;

            log("INFO: current_value := %d, sum := %ld\n", value, sum);
            f = '0';
            l = '0';
            value = 0;

            continue;
        }
        if (isdigit(d)) {
            if (f == '0') {
                f = d;
            }
            l = d;
        };
    }

    printf("Part 1: %ld\n", sum); // 54697

    fclose(file);
    return 0;
}
