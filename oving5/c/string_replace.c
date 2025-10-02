#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* replace_string(const char *str) {
    size_t len = 0;
    for (const char *c = str; *c; ++c) {
        switch (*c) {
            case '<': len += 4; break;   // &lt;
            case '>': len += 4; break;   // &gt;
            case '&': len += 5; break;   // &amp;
            default: len += 1;
        }
    }

    char* output = malloc(len + 1);
    if (!output) return NULL;

    char* p = output;
    for (const char *c = str; *c; ++c) {
        switch (*c) {
            case '<': strcpy(p, "&lt;"); p += 4; break;
            case '>': strcpy(p, "&gt;"); p += 4; break;
            case '&': strcpy(p, "&amp;"); p += 5; break;
            default: *p++ = *c;
        }
    }
    *p = '\0';
    return output;
}

int main() {
    char str[32];
    if (fgets(str, sizeof(str), stdin)) {
        char* replaced = replace_string(str);
        if (replaced) {
            printf("%s\n", replaced);
            free(replaced);
        }
    }
    return 0;
}
