#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <sys/ucontext.h>

#define LOG 0
#define READ_BUFFER_SIZE 1024
char READ_BUFFER[READ_BUFFER_SIZE];

#if !LOG
#define log(s, ...) {}
#else
#define log(s, ...) printf(s, __VA_ARGS__)
#endif

char *DIGITS[9] = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
};

int main(void) {
    FILE *file = fopen("content/day_1.txt", "rb");

    if (!file) {
        fprintf(stderr, "ERROR: Unable to open file\n");
        return 1;
    }

    long sum = 0;
    char first_digit = '0', last_digit = '0';
    while (1) {
        size_t bytes_read = fread(READ_BUFFER, sizeof(char), READ_BUFFER_SIZE, file);

        if (bytes_read == 0) {
            break;
        }

        for (size_t i = 0; i < bytes_read; i++) {
            char d = READ_BUFFER[i];

            if (d == '\n') {
                int value = (first_digit - '0') * 10 + (last_digit - '0');
                sum += value;

                log("INFO: current_value := %d, sum := %ld\n", value, sum);
                first_digit = '0';
                last_digit = '0';
                value = 0;

                continue;
            }

            if (isdigit(d)) {
                if (first_digit == '0') {
                    first_digit = d;
                }
                last_digit = d;
            };

        }

        if (bytes_read < READ_BUFFER_SIZE) {
            if (feof(file) == 0) {
                fprintf(stderr, "ERROR: reading file\n");
            } else {
                break;
            }
        }
    }

    printf("Part 1: %ld\n", sum); // 54697

    fclose(file);
    return 0;
}
