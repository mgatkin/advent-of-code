#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define NUM_WIRES 2
#define NUM_CMDS 4096
#define CMD_LEN 10
#define MAX_INTERSECTIONS 256
#define MAX_POSITIONS 500000

void find_next_position(int current_x, int current_y, char direction, int *next_x, int *next_y);

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Syntax:  day03 <input file>\n");
        return -1;
    }

    FILE *in = fopen(argv[1], "rt");
    char data[2][65536];

    if (in) {
        for (int w = 0; w < NUM_WIRES; w++) {
            fgets(data[w], 65536, in);
        }
        fclose(in);

        for (int w = 0; w < NUM_WIRES; w++) {
            int len = strlen(data[w]);
            if (data[w][len - 1] == '\n') {
                data[w][len - 1] = '\0';
            }
        }

#if DEBUG
        for (int w = 0; w < NUM_WIRES; w++) {
            printf("%s\n", data[w]);
        }
#endif

        char wire_directions[NUM_WIRES][NUM_CMDS][CMD_LEN];
        for (int w = 0; w < NUM_WIRES; w++) {
            char *saveptr;
            char *str = data[w];
            for (int t = 0; ; t++) {
                char *token = strtok_r(str, ",", &saveptr);
                if (token == NULL) {
                    break;
                }
                strncpy(wire_directions[w][t], token, 10);
                str = NULL;
            }
        }

        int wires[NUM_WIRES][MAX_POSITIONS][2];
        int wire_length[NUM_WIRES];
        for (int w = 0; w < NUM_WIRES; w++) {
            wires[w][0][0] = 0;
            wires[w][0][1] = 0;
            wire_length[w] = 1;
        }
        for (int w = 0; w < NUM_WIRES; w++) {
            int current_x = 0;
            int current_y = 0;
            int next_x, next_y;
            printf("Tracing wire %d\n", w + 1);
            for (int c = 0; c < NUM_CMDS; c++) {
                char *s = wire_directions[w][c];
                if (strlen(s) == 0) {
                    break;
                }
                char direction = s[0];
                int length = atoi(s + 1);
#if DEBUG
                printf("%d: %c%d\n", c + 1, direction, length);
#endif
                for (int i = 0; i < length; i++) {
                    find_next_position(current_x, current_y, direction, &next_x, &next_y);
                    wires[w][wire_length[w]][0] = next_x;
                    wires[w][wire_length[w]][1] = next_y;
                    current_x = next_x;
                    current_y = next_y;
                    wire_length[w] = wire_length[w] + 1;
                }
            }
        }

#if DEBUG
        for (int w = 0; w < NUM_WIRES; w++) {
            printf("wire%d has a length of %d\n", w + 1, wire_length[w]);
            for (int c = 0; c < wire_length[w] - 1; c++) {
                printf("(%d, %d), ", wires[w][c][0], wires[w][c][1]);
            }
            printf("(%d, %d)\n", wires[w][wire_length[w] - 1][0], wires[w][wire_length[w] - 1][1]);
        }
#endif

        int intersections[MAX_INTERSECTIONS];
        for (int i = 0; i < MAX_INTERSECTIONS; i++) {
            intersections[i] = 0;
        }
        printf("Finding intersections...\n");
        int intersection_count = 0;
        int shortest_distance = INT_MAX;
        int closest_point = 0;
        for (int s = 1; s < wire_length[0]; s++) {
            for (int d = 1; d < wire_length[1]; d++) {
                if ((wires[0][s][0] == wires[1][d][0]) &&
                        (wires[0][s][1] == wires[1][d][1])) {
                    intersections[intersection_count++] = s;
                    int distance = abs(wires[0][s][0]) + abs(wires[0][s][1]);
                    if (distance < shortest_distance) {
                        closest_point = s;
                        shortest_distance = distance;
                    }
                }
            }
        }
#if DEBUG
        for (int i = 0; i < intersection_count; i++) {
            printf("(%d, %d)\n", wires[0][intersections[i]][0], wires[0][intersections[i]][1]);
        }
#endif
        if (closest_point > 0) {
            printf("(%d, %d) %d\n",
                    wires[0][closest_point][0],
                    wires[0][closest_point][1],
                    shortest_distance);
        } else {
            printf("No intersection detected.\n");
        }
    }

    return 0;
}

void find_next_position(int current_x, int current_y, char direction, int *next_x, int *next_y)
{
    switch (direction) {
        case 'R':
            *next_x = current_x + 1;
            *next_y = current_y;
            break;
        case 'U':
            *next_x = current_x;
            *next_y = current_y + 1;
            break;
        case 'L':
            *next_x = current_x - 1;
            *next_y = current_y;
            break;
        case 'D':
            *next_x = current_x;
            *next_y = current_y - 1;
            break;
    }
}
