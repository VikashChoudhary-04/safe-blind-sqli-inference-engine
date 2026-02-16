# Safe Blind SQLi Inference Engine

A **safety-focused automation framework** for blind SQL injection inference designed for **authorized security labs and red-team engagements**.

This project demonstrates how professional security teams safely automate **proof-of-impact extraction**, traffic shaping, and **evidence collection** during testing.

---

## ⚠️ Disclaimer

This tool is intended **ONLY for authorized environments** such as:

* Security labs
* Training platforms
* Internal red-team engagements
* Systems you have explicit permission to test

Do **NOT** use this tool against systems without authorization.

---

## 🎯 Project Goal

Blind SQL injection testing is:

* repetitive
* slow
* error-prone
* difficult to document

This tool automates the **measurement and evidence collection** process while enforcing **safety controls and rate limiting**.

Key philosophy:

> Reliability, safety, and reproducibility matter more than speed.

---

## ✨ Features

* Config-driven blind SQLi automation framework
* Cookie / Header / URL parameter injection support
* Baseline response measurement
* Boolean-based inference engine
* Character-by-character extraction
* Traffic shaping & jitter
* Evidence-driven workflow
* Designed for labs and authorized testing environments

---

## 📦 Installation
```
git clone https://github.com/VikashChoudhary-04/safe-blind-sqli-inference-engine.git
cd safe-blind-sqli-inference-engine

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```
### Verify installation
```
python3 -m blind_extractor.main
```
---

## 📁 Repository Structure
```txt
safe-blind-sqli-inference-engine/
│
├── blind_extractor/
│   ├── **init**.py
│   ├── main.py
│   ├── config_loader.py
│   ├── logger.py
│   ├── request_engine.py
│   ├── baseline.py
│   ├── inference_engine.py
│   ├── extractor.py
│   ├── scheduler.py      (future feature)
│   ├── checkpoint.py     (future feature)
│   └── oob_listener.py   (future feature)
│
├── config.yaml
├── requirements.txt
├── LICENSE
└── README.md
```
---

## 🧠 When Should You Use This Tool?

Use this tool **after manually confirming a blind SQL injection vulnerability.**

This tool is **NOT a vulnerability scanner**.

It is designed to:

* Automate inference
* Reduce repetitive testing
* Collect reproducible evidence

---

## ⚙️ Configuration

All behaviour is controlled via **config.yaml**.
Users adapt this file for their specific target.

### Example configuration
```
target:
  url: "https://target-lab-url/"

injection:
  type: "cookie"
  name: "TrackingId"
  base_value: ""

inference:
  true_string: "Welcome back!"

extraction:
  charset: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  max_length: 25
  query: "' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{pos},1)='{char}"
```
---

## 🔍 Configuration Explanation

### Injection settings

| Field      | Meaning                                |
| ---------- | -------------------------------------- |
| type       | cookie / param / header                |
| name       | vulnerable parameter / cookie / header |
| base_value | normal value before payload            |

Examples:

Inject into URL parameter:
`type: param`
`name: id`

Inject into header:
`type: header`
`name: User-Agent`

Inject into cookie:
`type: cookie`
`name: session`

---

### TRUE detection

The engine detects when a condition is TRUE using a response string.

Example:

`true_string: "Welcome back!"`

Change this depending on the target behaviour.

---

### Extraction query

Defines the SQL condition tested for each character.

Example:

`query: "' AND SUBSTRING(database(),{pos},1)='{char}"`

Users modify this depending on:

* DB type
* Data being extracted
* Lab or engagement goals

---

## 🐢 Traffic Safety Settings
```
traffic:
  jitter_min_ms: 100
  jitter_max_ms: 400
```
These settings:

* Slow down requests
* Add randomness
* Protect target stability
* Reduce detection risk

---

## ▶️ Running the Tool
```
python3 -m blind_extractor.main
```
---

## 🔬 Execution Workflow

### Phase 1 — Baseline

The tool learns normal response behaviour to avoid false positives.

### Phase 2 — Condition Testing

The tool tests database conditions such as:

Is character N equal to X?

TRUE/FALSE is detected using response differences.

### Phase 3 — Character Extraction

Example output:
```
[+] Found: a
[+] Found: ad
[+] Found: adm
Extraction complete: admin
```
---

## 🧪 Example Workflow

Typical professional usage:

1. Confirm blind SQL injection manually
2. Configure config.yaml for the target
3. Run the tool
4. Extract minimal proof-of-impact
5. Use results in a pentest report

---

## 🛠 Troubleshooting

If extraction returns empty:

* Injection point may be wrong
* TRUE detection string may be incorrect
* SQL query may not match DB type
* Increase timeout or jitter

---

# 📜 License

MIT License
