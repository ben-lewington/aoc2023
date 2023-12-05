#include <stdio.h>
#ifndef AOC_LOG
#define AOC_LOG 0
#endif

#if !AOC_LOG
#define log(s, ...) {}
#define elog(s, ...) {}
#else
#define log(s, ...) printf(s, __VA_ARGS__)
#define elog(s, ...) fprintf(stderr, s, __VA_ARGS__)
#endif

typedef struct {
    FILE* file;
} Lines;
