CYB Network Monitor

A lightweight Python-based network monitoring tool designed to check host availability and service status.

This project was built as part of practical cybersecurity and infrastructure learning, focusing on reliability monitoring and automation.

Overview

CYB Network Monitor allows users to:

Monitor multiple hosts simultaneously

Check if a host is reachable (ping)

Verify whether a specific port is open

Log status results with timestamps

Run checks continuously at defined intervals

Use a simple command-line interface

The tool is intended for educational purposes and authorized internal monitoring.

Features

Multi-target monitoring

Optional port availability checking

Configurable monitoring interval

Multithreaded execution

Log file generation

Clean modular architecture

Input validation

CLI-based usage

Usage

Basic monitoring:

python main.py -t google.com


Monitor multiple hosts:

python main.py -t google.com 8.8.8.8


Monitor specific port:

python main.py -t google.com -p 80


Set custom interval (in seconds):

python main.py -t google.com -p 80 -i 10
