# ✅ Cambrian.org Waitlist Registration

A Python + Playwright script for automatically registering email addresses to the waitlist at [https://cambrian.org](https://cambrian.org).

---

## 🚀 Features

- 💬 Email registration support from `emails.txt`
- 🌐 Optional proxy usage from `proxies.txt` (looped if fewer proxies than emails)
- 🧠 Unique Chrome user-agent and randomized screen resolution
- 🖱️ Simulated user actions: click on `WAITLIST`, input email, submit
- ✅ Registration success check (via the `Success` button)
- 🧾 Logging of successful and failed attempts:
  - `results_*.txt` — successes
  - `errors_*.txt` — failures
- ⚙️ Multithreading via `ThreadPoolExecutor`
- 🐢 Random delays between actions (anti-bot mimicry)

---

## 📂 Project Structure

| File              | Description                                    |
|-------------------|------------------------------------------------|
| `main.py`         | Main script                                    |
| `emails.txt`      | List of email addresses (one per line)         |
| `proxies.txt`     | (optional) Proxy list in URL format            |
| `utils/logger.py` | `logger` utility                               |
| `results_*.txt`   | Successful registrations                       |
| `errors_*.txt`    | Registration failures                          |

---

## 📋 File Formats

### `emails.txt`

```
example1@gmail.com
example2@yahoo.com
...
```

### `proxies.txt` (if USE_PROXY = True)

```
http://user:pass@ip:port
socks5://ip:port
...
```

---

## ⚙️ Installation

1. Make sure Python 3.11+ is installed
2. Install dependencies:

```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
playwright~=1.52.0
loguru~=0.7.3
```

3. Install Google Chrome (used with `channel="chrome"`)

---

## ▶️ Run

```bash
python main.py
```

This script is configured with:

- `MAX_THREADS = 2` — you can change this in `main.py`
- `USE_PROXY = False` — set to `True` to enable proxy usage from `proxies.txt`. If there are fewer proxies than emails, they will cycle.

---

## 📝 Output Files

- `results_<timestamp>.txt` — successful registrations (email:proxy)
- `errors_<timestamp>.txt` — failed attempts (e.g. if Success button not found)

---

## 📄 License

Provided for educational and research purposes only.