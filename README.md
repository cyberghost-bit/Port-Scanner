# 🔍 Port Scanner (Python)

A simple yet efficient **multi-threaded port scanner** built with Python’s `socket` and `concurrent.futures` modules.  
It scans a predefined set of common TCP ports on a given host and identifies the running services.

---

## 📦 Features

- ✅ Multi-threaded scanning for high speed  
- ✅ Detects open TCP ports  
- ✅ Identifies common services automatically  
- ✅ Timeout handling for stability  
- ✅ Clean and minimal CLI output  

---

## 🧰 Requirements

- Python 3.7+
- Works on Linux, macOS, and Windows (no extra dependencies)

---

## ⚙️ Installation

Clone or download this repository:

```bash
git clone https://github.com/cyberghost-bit/Port-Scanner.git
cd port-scanner
```
## 🚀 Usage

Run the scanner with a hostname or IP address:

```bash
python3 port-scanner.py <HOST>
```

* `<HOST>` can be a hostname (example: `example.com`) or an IP address (`192.168.1.10`).

### Examples

Scan a hostname:

```bash
python3 port-scanner.py example.com
```

Scan an IP:

```bash
python3 port-scanner.py 192.168.1.10
```

### Running from Windows (PowerShell / CMD)

If `python3` is not recognized, use `python`:

```powershell
python port-scanner.py scanme.nmap.org
```

---



