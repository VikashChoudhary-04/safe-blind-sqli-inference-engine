# Safe Blind SQLi Inference Engine

## Overview
A safety-focused automation framework for blind SQL injection inference in authorized red-team labs.

## Features
- Rate limiting & jitter
- Baseline noise detection
- Evidence logging
- Binary search extraction
- Proxy support (Burp)
- Config-driven operation

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/safe-blind-sqli-inference-engine.git

# 2. Move into the project directory
cd safe-blind-sqli-inference-engine

# 3. (Recommended) Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python -m blind_extractor.main
```

---

# 📁 Repository Structure

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
│   ├── extractor.py              # Character-by-character extraction engine
│   ├── scheduler.py              # (v2 placeholder) task scheduling
│   ├── checkpoint.py             # (v2 placeholder) resume capability
│   └── oob_listener.py           # (v2 placeholder) OOB integration
│
├── config.yaml                   # Tool configuration (targets, limits, safety)
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── LICENSE                       # MIT license
└── .gitignore                    # Ignored files and folders
```

---

## Disclaimer
For authorized testing environments only.
