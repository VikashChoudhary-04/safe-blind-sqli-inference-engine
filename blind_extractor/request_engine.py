import requests, time, random
from dataclasses import dataclass

@dataclass
class ResponseData:
    time: float
    length: int
    error: bool

class RequestEngine:
    def __init__(self, config):
        self.url = config["target"]["url"]
        self.param = config["target"]["injectable_param"]
        self.base = config["target"]["base_value"]

        self.timeout = config["network"]["timeout"]
        self.retries = config["network"]["retries"]
        self.proxy = config["network"]["proxy"]

        self.jitter_min = config["traffic"]["jitter_min_ms"]/1000
        self.jitter_max = config["traffic"]["jitter_max_ms"]/1000

        self.session = requests.Session()
        if self.proxy:
            self.session.proxies = {"http": self.proxy, "https": self.proxy}

    def _sleep(self):
        time.sleep(random.uniform(self.jitter_min, self.jitter_max))

    def send_payload(self, payload):
        for _ in range(self.retries):
            try:
                self._sleep()
                start = time.time()
                r = self.session.get(self.url, params={self.param: payload}, timeout=self.timeout, verify=False)
                return ResponseData(time.time()-start, len(r.text), False)
            except:
                pass
        return ResponseData(0,0,True)
