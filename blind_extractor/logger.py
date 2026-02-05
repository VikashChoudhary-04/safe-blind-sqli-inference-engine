import logging, json
from pathlib import Path
from datetime import datetime

class EvidenceLogger:
    def __init__(self, text_path, json_path):
        Path("logs").mkdir(exist_ok=True)

        self.logger = logging.getLogger("BlindSQLi")
        self.logger.setLevel(logging.INFO)

        fh = logging.FileHandler(text_path)
        fh.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
        self.logger.addHandler(fh)

        self.json_path = json_path
        self.entries = []

    def log(self, data: dict):
        entry = {"time": datetime.utcnow().isoformat(), **data}
        self.entries.append(entry)
        self.logger.info(json.dumps(data))

    def save(self):
        with open(self.json_path, "w") as f:
            json.dump(self.entries, f, indent=2)
