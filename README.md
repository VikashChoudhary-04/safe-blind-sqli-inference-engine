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

* Baseline response measurement
* Time-based inference engine
* Character-by-character extraction
* Traffic shaping & jitter
* Evidence logging (JSON + text)
* Proxy support (Burp Suite)
* Config-driven behaviour
* Safety-focused design

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/VikashChoudhary-04/safe-blind-sqli-inference-engine.git

# Move into project folder
cd safe-blind-sqli-inference-engine

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Verify installation

```bash
python3 -m blind_extractor.main
```

---

## 📁 Repository Structure

```text
safe-blind-sqli-inference-engine/
│
├── blind_extractor/              # Main application package
│   ├── __init__.py
│   ├── main.py                   # Entry point / orchestrator
│   ├── config_loader.py          # Loads YAML configuration
│   ├── logger.py                 # Evidence & JSON logging system
│   ├── request_engine.py         # HTTP communication & measurement
│   ├── baseline.py               # Establishes normal response baseline
│   ├── inference_engine.py       # TRUE/FALSE decision logic
│   ├── extractor.py              # Character extraction engine
│   ├── scheduler.py              # (v2 placeholder) scheduling system
│   ├── checkpoint.py             # (v2 placeholder) resume capability
│   └── oob_listener.py           # (v2 placeholder) OOB integration
│
├── config.yaml                   # Tool configuration
├── requirements.txt              # Python dependencies
├── LICENSE                       # MIT license
└── README.md                     # Documentation
```

---

## 🧠 When Should You Use This Tool?

Use this tool **after** you have manually confirmed a blind SQL injection vulnerability.

This tool is **NOT a scanner**.

It is designed to:

* Automate inference
* Reduce manual repetition
* Collect reproducible evidence

---

## ⚙️ Configuration

All behaviour is controlled via **config.yaml**.

Example:

```yaml
target:
  url: "https://lab.test/products"
  injectable_param: "id"
  base_value: "1"
```

### Field Explanation

| Field            | Description           |
| ---------------- | --------------------- |
| url              | Target endpoint       |
| injectable_param | Vulnerable parameter  |
| base_value       | Normal baseline value |

---

## 🐢 Traffic Safety Settings

```yaml
traffic:
  max_requests_per_minute: 30
  jitter_min_ms: 200
  jitter_max_ms: 800
```

These settings:

* Slow down requests
* Add randomness
* Reduce detection risk
* Protect lab stability

---

## ▶️ Running the Tool

```bash
python3 -m blind_extractor.main
```

---

## 🔬 What Happens During Execution

### Phase 1 — Baseline Detection

The tool learns normal response behaviour:

* Average response time
* Normal response size

This prevents false positives.

---

### Phase 2 — Condition Testing

The tool tests database conditions like:

```
Is the first character of the database name = 'a' ?
```

It detects TRUE/FALSE using response timing.

---

### Phase 3 — Character Extraction

Example output:

```
[+] Found: a
[+] Found: ac
[+] Found: acc
Extraction complete: accounts
```

---

## 📊 Evidence Logging

After execution:

```
logs/run.log   → Human readable log
logs/run.json  → Machine readable evidence
```

Example JSON entry:

```json
{
  "payload": "SUBSTRING(database(),1,1)='a'",
  "time": 2.63,
  "decision": true
}
```

Logs are designed for:

* Pentest reports
* Reproducibility
* Audit trails

---

## 🧪 Example Workflow

Typical professional workflow:

1. Confirm blind SQL injection manually.
2. Configure vulnerable parameter.
3. Run the tool.
4. Extract minimal proof-of-impact.
5. Use logs as report evidence.

---

## 🛠 Troubleshooting

If extraction returns empty:

* Target may not be vulnerable
* Payload may not match database type
* Increase timeout or jitter values

---

# 📜 License

MIT License

---
