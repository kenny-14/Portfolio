#include <stdio.h>

float to_fahrenheit(float c) {
    return (c * 9/5) + 32;
}

float find_max(float arr[], int size) {
    float max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

float find_average(float arr[], int size) {
    float sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum / size;
}

int main() {
    float temp[8] = {22.5, 35.0, 18.3, 41.2, 29.7, 33.1, 15.8, 27.4};
    int size = 8;

    for (int i = 0; i < size; i++) {
        float f = to_fahrenheit(temp[i]);
        printf("%.2f°C = %.2f°F", temp[i], f);

        if (temp[i] > 30)
            printf(" [HOT]");

        printf("\n");
    }

    printf("Max: %.2f\n", find_max(temp, size));
    printf("Average: %.2f\n", find_average(temp, size));

    return 0;
}