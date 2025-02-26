# Use Ubuntu as base
FROM ubuntu:22.04

# Install dependencies
RUN apt update && apt install -y \
    python3 python3-pip python3-venv git curl wget nano \
    qemu qemu-system-xtensa \
    mosquitto mosquitto-clients \
    software-properties-common \
    libgcrypt20 libglib2.0-0 libpixman-1-0 libsdl2-2.0-0 libslirp0 \
    mongodb-clients  # <-- MongoDB client installed

# Clone ESP-IDF
RUN git clone --recursive https://github.com/espressif/esp-idf.git /root/esp-idf

# Install ESP-IDF tools
RUN python /root/esp-idf/tools/idf_tools.py install qemu-xtensa qemu-riscv32

# Set up environment variables
ENV IDF_PATH=/root/esp-idf
WORKDIR /root/esp

# Copy ESP32 simulation code
COPY esp32 /root/esp/hello_world

# Set up QEMU
CMD [ "bash" ]

