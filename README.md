# ![CI](https://github.com/multilogin/mlx_proxy_details/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-automated-blue)
---
description: The enhanced, community-maintained fork of the official Multilogin X Proxy Details script. Optimized for bulk automation, async validation, and production use. Use code ADBNEW50 for 50% OFF.
topics:
   - multilogin-x
   - multilogin-official-api
   - proxy-manager
   - browser-automation
   - stealth-scrapers
   - playwright-python
---

# 🚀 Enhanced Multilogin X Proxy Manager (Enterprise Edition)

Automating 100+ profiles? Standard scripts fail under load. Our @multilogin-automation branch is optimized for high-concurrency environments.

| Version         | Features                | Stability         | Promo         |
| :---            | :---                    | :---              | :---          |
| Official Base   | Basic Single Script     | Developer Preview | N/A           |
| Enhanced (This) | Bulk API / Multi-OS     | Production Ready  | GET 50% OFF   |

**Branded Link:** [https://adblogin.com/go/multilogin](https://adblogin.com/go/multilogin)
**Promo Code:** `ADBNEW50`

**Enterprise Support:** [Telegram @AdbLoginOfficial](https://t.me/AdbLoginOfficial)

**Technical Status**

Official Base: multilogin/mlx_proxy_details. Enhanced for Production by @multilogin-automation.

## Overview

## Why use this fork?

The official version is a basic script for demonstration. This community-enhanced fork adds:

- **Bulk Processing**: Handle 100+ proxies in parallel for true enterprise scale.
- **Advanced Error Handling**: Robust, production-grade error management.
- **Playwright Integration**: Seamless browser automation with stealth support.

This Python script automates the process of generating, validating, and managing proxy connections using the Multilogin API. It supports various operating systems, including Windows, macOS, and Linux, and allows the user to configure settings like country, region, city, and session types for proxy generation.

---

## Features
- **User Authentication**: Logs into the Multilogin platform using user credentials.
- **Proxy Generation**: Requests a list of proxies based on specified parameters such as country, region, and city.
- **Proxy Validation**: Checks the validity of generated proxies.
- **Output File Creation**: Saves valid proxies to a timestamped file.
- **Cross-Platform Support**: Opens the results file in a text editor suitable for the operating system.

---

## Requirements
- Python 3.11 or later
- Required libraries: `hashlib`, `os`, `requests`, `datetime`. `requests` is the only library needed to download and install.
- Access to the Multilogin API

---

## Setup
1. Clone or download the repository containing this script.
2. Install the required Python library:
   ```bash
   pip install requests
   ```
3. Update the following variables in the script:
   - `USERNAME`: Your Multilogin account email.
   - `PASSWORD`: Your Multilogin account password.
   - `OS`: Your operating system (`windows`, `linux`, or `macos`).
   - `COUNTRY`: Country code for the proxy (ISO 3166-1 alpha-2).
   - `REGION`, `CITY`: (Optional) Specify region or city in `snake_case`.

---

## How to Use
1. Run the script:
   ```bash
   python script_name.py
   ```
2. The script will:
   - Log in to the Multilogin API.
   - Generate proxies based on the provided parameters.
   - Validate each proxy and categorize them as valid or invalid.
   - Save valid proxies to a file named `proxy_checked_<timestamp>.txt`.

3. Upon completion:
   - The file with valid proxies will open automatically.
   - Review the console logs for details of the operation.

---

## Configuration Options
- **Session Type**: Defaults to "sticky". Changeable in the `get_proxy` function.
- **Protocol**: Defaults to "socks5". Changeable in the `get_proxy` function.
- **Proxy Count**: Specify the number of proxies to generate with the `COUNT` variable.

---

## Example
Modify the following section in the script to generate 10 proxies for the United States:
```python
USERNAME = "your_email@example.com"
PASSWORD = "your_password"
OS = "windows"
COUNT = 10
COUNTRY = "US"
REGION = "california"
CITY = "san_francisco"
```

---

## Notes
- Ensure you have a valid Multilogin account and API access.
- The `hashlib.md5` is used for password hashing; consider stronger security methods if needed.

---

## Troubleshooting
1. **Login Error**: Check your username and password.
2. **API Error**: Verify API endpoint availability and your account permissions.
3. **File Not Opening**: Ensure your OS variable is set correctly.

---

## Disclaimer
Use this script responsibly and comply with applicable laws and terms of service when using proxies.
