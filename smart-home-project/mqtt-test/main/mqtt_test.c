#include <stdio.h>
#include <inttypes.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_netif.h"
#include "esp_event.h"
#include "mqtt_client.h"

#define MQTT_BROKER "mqtt://localhost:1883"

esp_mqtt_client_handle_t client;

static void mqtt_event_handler(void *handler_args, esp_event_base_t base, int32_t event_id, void *event_data) {
    printf("MQTT event received, event_id=%" PRId32 "\n", event_id);

    if (event_id == MQTT_EVENT_CONNECTED) {
        printf(" MQTT Connected! Subscribing to 'emqx/esp32'...\n");
        esp_mqtt_client_subscribe(client, "emqx/esp32", 0);
        esp_mqtt_client_publish(client, "emqx/esp32", "Hello from ESP32 (QEMU)!", 0, 0, 0);
    } else if (event_id == MQTT_EVENT_DATA) {
        printf(" Message received: %s\n", (char *)event_data);
    }
}

void app_main(void) {
    printf("ESP32 MQTT Emulation Started...\n");

    // **Ensure TCP/IP stack is initialized**
    esp_err_t ret = esp_netif_init();
    if (ret != ESP_OK) {
        printf(" esp_netif_init failed: %s\n", esp_err_to_name(ret));
        return;
    }

    ret = esp_event_loop_create_default();
    if (ret != ESP_OK) {
        printf(" esp_event_loop_create_default failed: %s\n", esp_err_to_name(ret));
        return;
    }

    // **MQTT Configuration**
    esp_mqtt_client_config_t mqtt_cfg = {
        .broker.address.uri = MQTT_BROKER
    };

    client = esp_mqtt_client_init(&mqtt_cfg);
    if (client == NULL) {
        printf(" MQTT client initialization failed!\n");
        return;
    }

    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, mqtt_event_handler, NULL);
    esp_mqtt_client_start(client);

    // **Keep Running**
    while (1) {
        vTaskDelay(2000 / portTICK_PERIOD_MS);
    }
}
