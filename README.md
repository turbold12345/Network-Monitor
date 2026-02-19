# CYB Network Monitor

A lightweight Python-based network monitoring tool designed to check host availability and service status.

This project was developed as part of practical cybersecurity and infrastructure learning, focusing on reliability monitoring and automation.

---

## 📌 Overview

CYB Network Monitor allows users to:

- Monitor multiple hosts simultaneously
- Check if a host is reachable (ping)
- Verify whether a specific port is open
- Log status results with timestamps
- Run checks continuously at defined intervals
- Use a simple command-line interface

This tool is intended for educational purposes and authorized internal monitoring.

---

## 🚀 Features

- Multi-target monitoring
- Optional port availability checking
- Configurable monitoring interval
- Multithreaded execution
- Log file generation
- Clean modular architecture
- Input validation
- CLI-based usage

---


---

## ⚙ Installation

Clone the repository:

git clone https://github.com/turbold12345/Network-Monitor.git

Navigate into the folder: cd Network-Monitor


No external dependencies are required (uses standard Python library).

---

## 🖥 Usage

Basic monitoring:python main.py -t google.com


Monitor multiple hosts: python main.py -t google.com 8.8.8.8


Monitor a specific port: python main.py -t google.com -p 80


Set custom interval (in seconds): python main.py -t google.com -p 80 -i 10

---

## 🔎 How It Works

1. Targets are validated before execution.
2. Each host is checked using ICMP ping.
3. If a port is specified, a TCP connection attempt is performed.
4. Results are displayed in the terminal.
5. Results are written to `logs/monitor.log` with timestamps.
6. Checks repeat based on the defined interval.

---
## ⚠ Disclaimer

This tool is intended strictly for educational purposes and authorized network monitoring only. Unauthorized use against systems without permission is not permitted.

---

