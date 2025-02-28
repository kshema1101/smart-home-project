#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void simulate_sensor_readings(float *temperature, float *humidity) {
    *temperature = 20.0 + (rand() % 10);  // Simulate 20-30°C
    *humidity = 40.0 + (rand() % 30);     // Simulate 40-70% RH
}

int main() {
    FILE *file;
    
    while (1) {
        float temperature, humidity;
        simulate_sensor_readings(&temperature, &humidity);
        
        // Open the file and write sensor data
        file = fopen("/Users/nikhil/smart-home-project/smart-home-project/esp32/sensor_simulation/sensor_data.txt", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
        }
        
        fprintf(file, "%.2f,%.2f\n", temperature, humidity);
        fclose(file);

        printf("Sensor Data Saved: Temperature=%.2f°C, Humidity=%.2f%%\n", temperature, humidity);
        
        sleep(5);  // Simulate data update every 5 seconds
    }
    
    return 0;
}
