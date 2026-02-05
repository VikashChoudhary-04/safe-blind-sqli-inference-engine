class InferenceEngine:
    def __init__(self, requester, baseline, logger):
        self.req = requester
        self.base_time, self.std, self.base_len = baseline
        self.logger = logger

    def is_true(self, payload):
        r = self.req.send_payload(payload)
        decision = r.time > (self.base_time + self.std * 2)

        self.logger.log({
            "payload": payload,
            "time": r.time,
            "decision": decision
        })

        return decision
