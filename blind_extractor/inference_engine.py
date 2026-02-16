class InferenceEngine:
    def __init__(self, requester, baseline, logger, config):
        self.req = requester
        self.true_string = config["inference"]["true_string"]

    def is_true(self, payload):
        r = self.req.send_payload(payload)

        print("TESTING:", payload)

        if self.true_string.lower() in r.text.lower():
            print(" → TRUE")
            return True
        else:
            print(" → FALSE")
            return False
