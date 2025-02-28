#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

void app_main(void) {
    while (1) {
        printf(" Hello, ESP32 in QEMU! \n");
        vTaskDelay(2000 / portTICK_PERIOD_MS);
    }
}
