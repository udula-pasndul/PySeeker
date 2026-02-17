# 🔍 PySeeker — API-less Network Reconnaissance Tool

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Status](https://img.shields.io/badge/status-Educational-orange)]  

**PySeeker** is a lightweight, **API-less network reconnaissance tool** designed **for educational purposes only**.  
It helps you understand subdomain discovery, port scanning, service detection, and vulnerability awareness using Python.

> ⚠️ **Educational & Defensive Use Only — Do Not Scan Unauthorized Systems**

---

## 🚀 Features

- 🌐 Resolve domain names to IPs
- 🔎 Discover subdomains
- 🔐 TCP port scanning (custom port ranges)
- 🧾 Service and banner detection
- ⚠️ Awareness of potential vulnerabilities (banner-based CVE matching)
- 🧠 Lightweight and easy to study Python code

---

## 🛠 Installation

### 1️⃣ Install Python 3.9+

Check if Python is installed:

```bash
python --version
or

bash
Copy code
python3 --version
If not installed, download from Python.org and check "Add Python to PATH" during installation.

2️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/PySeeker.git
cd PySeeker
3️⃣ Install Required Python Packages
All dependencies are listed in requirements.txt. Install them:

bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
⚡ On Windows, if permission issues occur, add --user:

bash
Copy code
pip install --user -r requirements.txt
4️⃣ Run PySeeker
bash
Copy code
python main.py -d example.com -p 1-100
Example:

bash
Copy code
python main.py -d scanme.sh -p 1-100
Output includes:

Resolved target IP

Discovered subdomains

Open ports

Service banners

Potential vulnerability indicators (if detected)

📚 Educational Goals
PySeeker teaches:

DNS resolution concepts

Subdomain discovery basics

Port scanning fundamentals

Service banner recognition

Awareness of potential vulnerabilities (without exploiting)

🔒 This tool does NOT exploit systems. Only observes publicly available information.
