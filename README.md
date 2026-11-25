# CyberToolkit

A Python/Tkinter desktop toolkit built as my final project for the Cyber Communication Lab course at Ruppin Academic Center. It groups the day-to-day tools I needed during the course into a single dark-themed GUI.

## Features

- Hash and encrypt text with SHA-256 or Fernet (symmetric encryption)
- Caesar cipher brute-force attack with all 26 shifts
- Vigenère cipher decryption with a known key
- Fake data generation in several locales (en_US, it_IT, he_IL, ja_JP) with Faker
- Keyword search on a web page, with the matched context
- MSSP-related helpers
- Multi-threaded traffic simulation lab, for testing on a local environment

## Requirements

Python 3.10+, then:

pip install faker requests cryptography

Tkinter ships with most Python installs; on Debian/Ubuntu install python3-tk.

## Run

python cybertoolkit.py

## Disclaimer

This project was written for academic purposes and for controlled lab environments only. The attack and traffic simulation modules are meant to be run against your own machines or an isolated network. Do not use them against systems you do not own or have written permission to test.

## Author

Natan Ouaki — Computer Engineer, cybersecurity and AI specialization.
