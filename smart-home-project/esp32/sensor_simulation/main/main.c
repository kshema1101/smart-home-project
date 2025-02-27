#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

// Simulated sensor function
void simulate_sensors() {
    static int temp = 25;      // Starting temperature
    static int pressure = 1000; // Starting pressure (hPa)
    static int motion = 0;      // No motion initially

    temp += (rand() % 3 - 1);       // Random fluctuation
    pressure += (rand() % 5 - 2);   // Random fluctuation
    motion = rand() % 2;            // 0 or 1 (No motion or Motion detected)

    printf("\n[SENSOR DATA] Temperature: %d°C | Pressure: %dhPa | Motion: %s\n",
           temp, pressure, motion ? "Detected" : "None");
    fflush(stdout);  // 🔹 Ensure immediate output in QEMU
}

void app_main(void) {
    printf("🚀 ESP32 Sensor Simulation Started...\n");
    fflush(stdout);  // 🔹 Ensure startup message is printed immediately

    vTaskDelay(500 / portTICK_PERIOD_MS);  // Small delay to allow message to appear

    while (1) {
        printf("🟢 Running simulate_sensors()...\n"); // 🔹 Debug print statement
        fflush(stdout);

        simulate_sensors();
        vTaskDelay(2000 / portTICK_PERIOD_MS);
    }
}
