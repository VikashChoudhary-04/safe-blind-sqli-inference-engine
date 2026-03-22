class InferenceEngine:
    def __init__(self, requester, config, logger):
        self.requester = requester
        self.config = config
        self.logger = logger

        self.mode = config["inference"]["type"]
        self.true_string = config["inference"].get("true_string", "").lower()
        self.threshold = config["inference"].get("threshold", 2)

        self.baseline_length = None

    def is_true(self, payload):
        response = self.requester.send_payload(payload)

        text = response.text.lower()
        length = response.length
        time_taken = response.time

        # STRING MODE
        if self.mode == "string":
            return self.true_string in text

        # LENGTH MODE
        elif self.mode == "length":
            if self.baseline_length is None:
                self.baseline_length = length
            return abs(length - self.baseline_length) > 5

        # TIME MODE
        elif self.mode == "time":
            return time_taken > self.threshold

        return False
