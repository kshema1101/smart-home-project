
# Smart Home Project 🚀
# Smart Home Automation with ESP32 & QEMU in Docker 🏠🔧

## Overview
This project simulates an **ESP32-based Smart Home system** using **QEMU**, **MQTT**, and **MongoDB**, all running inside a **Dockerized environment**. The system enables **sensor data processing**, **remote device control**, and **real-time monitoring** through a **CI/CD pipeline**.

## 📌 Features
- **ESP32 Firmware Simulation** using QEMU 🖥️
- **MQTT Communication** for IoT Messaging 📡
- **MongoDB Database** for Sensor Data Storage 📊
- **FastAPI Backend** for Smart Home API 🚀
- **Home Assistant Integration** 🏡
- **CI/CD Pipeline** using GitHub Actions & Docker 🛠️

---

## 📦 Project Structure
smart-home-project/ │── docker/ │ ├── Dockerfile # Environment setup for ESP32 simulation │ ├── docker-compose.yml # Service configurations │── esp32/ │ ├── hello_world/ # ESP32 firmware project │ ├── qemu/ # QEMU emulator setup │── backend/ │ ├── app/ # FastAPI backend for Smart Home API │ ├── database/ # MongoDB integration │── mqtt/ │ ├── broker/ # Mosquitto MQTT broker setup │── ci-cd/ │ ├── github-actions/ # CI/CD pipeline scripts │── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/smart-home-project.git
cd smart-home-project
2️⃣ Build and Run Docker Containers 🐳
sh
Copy
Edit
docker-compose up -d
3️⃣ Run ESP32 Firmware in QEMU
sh
Copy
Edit
docker exec -it smart-home bash
cd /root/esp/hello_world
idf.py qemu monitor
4️⃣ Test MQTT Messaging
sh
Copy
Edit
mosquitto_pub -h localhost -t "home/livingroom" -m "Turn on light"
mosquitto_sub -h localhost -t "home/livingroom"
5️⃣ Start FastAPI Backend
sh
Copy
Edit
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000
6️⃣ Access Home Assistant UI
Open http://localhost:8123 in your browser.
